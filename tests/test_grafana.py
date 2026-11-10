"""Offline vendoring, extraction, integrity and launch policy tests; no live Grafana."""
import copy
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest
from unittest import mock
import zipfile
from link_support import create_symlink_or_skip

ROOT = Path(__file__).resolve().parents[1]


def module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


launcher = module("sds_grafana_test_launcher", "mcp/grafana/launch.py")
vendor = module("sds_grafana_test_vendor", "scripts/vendor_grafana.py")


def archive_bytes(binary, name="mcp-grafana", zip_archive=False, member_type=None, extra_name=None):
    output = io.BytesIO()
    if zip_archive:
        with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
            member = zipfile.ZipInfo(name)
            member.external_attr = (0o120777 if member_type == "symlink" else 0o100755) << 16
            archive.writestr(member, binary)
            if extra_name:
                archive.writestr(extra_name, b"must not be extracted")
    else:
        with tarfile.open(fileobj=output, mode="w:gz") as archive:
            member = tarfile.TarInfo(name)
            member.size = len(binary)
            if member_type == "symlink":
                member.type = tarfile.SYMTYPE
                member.linkname = "../../outside"
            archive.addfile(member, io.BytesIO(binary) if member_type != "symlink" else None)
            if extra_name:
                other = tarfile.TarInfo(extra_name)
                other.size = 1
                archive.addfile(other, io.BytesIO(b"x"))
    return output.getvalue()


class GrafanaTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.manifest_path = self.root / "release-manifest.json"
        self.vendor_dir = self.root / "vendor"
        self.vendor_dir.mkdir()
        self.cache = self.root / "cache"
        self.manifest = {"project": "grafana/mcp-grafana", "version": "v2.2.0", "assets": []}
        for key in sorted(launcher.PLATFORMS):
            windows = key.startswith("Windows_")
            name = "mcp-grafana_" + key + (".zip" if windows else ".tar.gz")
            member = "mcp-grafana.exe" if windows else "mcp-grafana"
            binary = ("synthetic offline binary " + key).encode("ascii")
            data = archive_bytes(binary, member, windows)
            asset = {"platform": key, "name": name, "binary_path": member,
                     "url": "https://github.com/grafana/mcp-grafana/releases/download/v2.2.0/" + name,
                     "size_bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                     "binary_size_bytes": len(binary), "binary_sha256": hashlib.sha256(binary).hexdigest()}
            self.manifest["assets"].append(asset)
            (self.vendor_dir / name).write_bytes(data)
        self.save_manifest()

    def save_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

    def asset(self, key="Linux_x86_64"):
        return next(asset for asset in self.manifest["assets"] if asset["platform"] == key)

    def prepare(self, system="Linux", machine="x86_64"):
        return launcher.prepare_binary(self.manifest_path, self.cache, system, machine)

    def replace_archive(self, asset, data):
        (self.vendor_dir / asset["name"]).write_bytes(data)
        asset.update(size_bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        self.save_manifest()

    def test_all_four_bundled_platforms_are_checked_without_network(self):
        with mock.patch.object(vendor, "build_opener", side_effect=AssertionError("network attempted")):
            result = vendor.check(self.manifest_path)
        self.assertEqual(result["archives_verified"], 4)
        self.assertEqual(result["network"], "none")

    def test_platform_aliases_and_unsupported_platform(self):
        self.assertEqual(launcher.platform_key("Linux", "aarch64"), "Linux_arm64")
        self.assertEqual(launcher.platform_key("Windows", "AMD64"), "Windows_x86_64")
        self.assertEqual(launcher.platform_key("Darwin", "arm64"), "Darwin_arm64")
        with self.assertRaises(ValueError):
            launcher.platform_key("Darwin", "x86_64")

    def test_extracts_and_verifies_exact_binary_for_tar_and_zip(self):
        for system, machine in (("Linux", "x86_64"), ("Linux", "arm64"), ("Darwin", "arm64"), ("Windows", "AMD64")):
            with self.subTest(system=system, machine=machine):
                binary, manifest, asset = self.prepare(system, machine)
                self.assertEqual(hashlib.sha256(binary.read_bytes()).hexdigest(), asset["binary_sha256"])
                self.assertIn(manifest["version"], binary.parts)
                self.assertEqual([p.name for p in binary.parent.iterdir()], [asset["binary_path"]])

    def test_missing_archive_refuses_even_with_valid_cached_binary(self):
        self.prepare()
        (self.vendor_dir / self.asset()["name"]).unlink()
        with self.assertRaisesRegex(ValueError, "missing"):
            self.prepare()

    def test_corrupt_archive_refused_before_extraction(self):
        path = self.vendor_dir / self.asset()["name"]
        data = bytearray(path.read_bytes())
        data[-1] ^= 1
        path.write_bytes(data)
        with self.assertRaisesRegex(ValueError, "checksum"):
            self.prepare()
        self.assertFalse(self.cache.exists())

    def test_corrupt_cached_binary_is_rejected_before_launch(self):
        binary, _, _ = self.prepare()
        data = bytearray(binary.read_bytes())
        data[0] ^= 1
        binary.write_bytes(data)
        with self.assertRaisesRegex(ValueError, "checksum"):
            self.prepare()

    def test_reuses_only_a_verified_cache_entry(self):
        binary, _, _ = self.prepare()
        with mock.patch.object(launcher, "extract_binary", side_effect=AssertionError("unexpected extraction")):
            second, _, _ = self.prepare()
        self.assertEqual(binary, second)

    def test_wrong_executable_digest_leaves_no_partial_binary(self):
        self.asset()["binary_sha256"] = "0" * 64
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "checksum"):
            self.prepare()
        self.assertFalse(any(path.is_file() for path in self.cache.rglob("*")))

    def test_symlinked_cache_and_bundle_paths_are_refused(self):
        outside = self.root / "outside"
        outside.mkdir()
        create_symlink_or_skip(self, self.cache, outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symbolic links"):
            self.prepare()
        self.cache.unlink()
        path = self.vendor_dir / self.asset()["name"]
        original = outside / path.name
        path.rename(original)
        create_symlink_or_skip(self, path, original)
        with self.assertRaisesRegex(ValueError, "Symbolic links"):
            self.prepare()

    def test_symlinked_cached_executable_is_refused(self):
        binary, _, _ = self.prepare()
        external = self.root / "external-binary"
        binary.rename(external)
        create_symlink_or_skip(self, binary, external)
        with self.assertRaisesRegex(ValueError, "Symbolic links"):
            self.prepare()

    def test_manifest_rejects_traversal_unpinned_urls_and_duplicate_platforms(self):
        original = copy.deepcopy(self.manifest)
        for changes in ({"binary_path": "../mcp-grafana"}, {"name": "../archive.tar.gz"},
                        {"url": "https://example.invalid/unpinned"}, {"size_bytes": True}):
            with self.subTest(changes=changes):
                self.manifest = copy.deepcopy(original)
                self.manifest["assets"][0].update(changes)
                self.save_manifest()
                with self.assertRaises(ValueError):
                    launcher.load_manifest(self.manifest_path)
        self.manifest = copy.deepcopy(original)
        self.manifest["assets"][1] = copy.deepcopy(self.manifest["assets"][0])
        self.save_manifest()
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            launcher.load_manifest(self.manifest_path)

    def test_tar_and_zip_reject_symlink_executable_members(self):
        for key, system, machine in (("Linux_x86_64", "Linux", "x86_64"), ("Windows_x86_64", "Windows", "AMD64")):
            with self.subTest(platform=key):
                asset = self.asset(key)
                self.replace_archive(asset, archive_bytes(b"x" * asset["binary_size_bytes"], asset["binary_path"],
                                                          key.startswith("Windows_"), "symlink"))
                with self.assertRaisesRegex(ValueError, "regular file"):
                    self.prepare(system, machine)

    def test_unselected_archive_traversal_member_is_never_extracted(self):
        asset = self.asset()
        data = archive_bytes(b"x" * asset["binary_size_bytes"], extra_name="../../escape")
        self.replace_archive(asset, data)
        with self.assertRaisesRegex(ValueError, "Unsafe archive"):
            self.prepare()
        self.assertFalse((self.root / "escape").exists())

    def test_launch_forces_read_only_tools_and_removes_ambient_routing_and_telemetry(self):
        original = {"SDS_GRAFANA_URL": "https://grafana.internal.example/grafana", "SDS_GRAFANA_TOKEN": "test-token",
                    "GRAFANA_URL": "https://wrong.example", "GRAFANA_TLS_SKIP_VERIFY": "true",
                    "grafana_service_account_token": "wrong-token", "OTEL_EXPORTER_OTLP_ENDPOINT": "https://wrong.example",
                    "otel_resource_attributes": "wrong-customer", "HTTP_PROXY": "https://wrong.example",
                    "https_proxy": "https://wrong.example", "ALL_PROXY": "socks5://wrong.example", "NO_PROXY": "*",
                    "DO_NOT_TRACK": "0", "do_not_track": "0", "PATH": "/test/path"}
        binary = Path("/verified/mcp-grafana")
        command, child = launcher.launch_configuration(binary, original)
        self.assertEqual(command, [str(binary), "-t", "stdio", "--disable-write",
                                   "--usage-stats=disabled",
                                   "--enabled-tools=search,datasource,dashboard,elasticsearch"])
        self.assertEqual(child["GRAFANA_URL"], original["SDS_GRAFANA_URL"])
        self.assertEqual(child["GRAFANA_SERVICE_ACCOUNT_TOKEN"], "test-token")
        self.assertEqual(child["GRAFANA_USAGE_STATS"], "disabled")
        self.assertEqual(child["DO_NOT_TRACK"], "1")
        self.assertFalse(any(key.upper().startswith("OTEL_") or key.upper() in launcher.PROXY_NAMES for key in child))
        self.assertNotIn("GRAFANA_TLS_SKIP_VERIFY", child)
        self.assertNotIn("grafana_service_account_token", child)
        self.assertNotIn("SDS_GRAFANA_TOKEN", child)
        self.assertNotIn("do_not_track", child)
        self.assertEqual(child["PATH"], original["PATH"])

    def test_invalid_endpoint_or_token_is_refused(self):
        valid = {"SDS_GRAFANA_URL": "https://grafana.example", "SDS_GRAFANA_TOKEN": "test-token"}
        for url in ("http://grafana.example", "https://user:password@grafana.example", "https://grafana.example?q=x",
                    "https://grafana.example#x", "https://grafana.example?", "https://grafana.example\\bad", "https://grafana.example\n"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                launcher.launch_configuration(Path("binary"), {**valid, "SDS_GRAFANA_URL": url})
        for token in ("", "  ", "bad\ntoken", "bad\x00token"):
            with self.subTest(token=repr(token)), self.assertRaises(ValueError):
                launcher.launch_configuration(Path("binary"), {**valid, "SDS_GRAFANA_TOKEN": token})

    def test_optional_ca_requires_regular_file_and_is_passed_explicitly(self):
        ca = self.root / "ca.pem"
        ca.write_text("synthetic test CA path; not used for TLS")
        environment = {"SDS_GRAFANA_URL": "https://grafana.example", "SDS_GRAFANA_TOKEN": "token", "SDS_GRAFANA_CA_FILE": str(ca)}
        command, _ = launcher.launch_configuration(Path("binary"), environment)
        self.assertEqual(command[-2:], ["--tls-ca-file", str(ca)])
        ca.unlink()
        with self.assertRaises(ValueError):
            launcher.launch_configuration(Path("binary"), environment)

    def test_check_mode_does_not_require_credentials_or_execute_binary(self):
        binary, manifest, asset = self.prepare()
        with mock.patch.object(sys, "argv", ["launch.py", "--check"]), \
                mock.patch.object(launcher, "prepare_binary", return_value=(binary, manifest, asset)), \
                mock.patch.object(launcher, "launch_configuration", side_effect=AssertionError("credentials requested")), \
                mock.patch.object(launcher, "execute", side_effect=AssertionError("binary executed")), \
                mock.patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertEqual(launcher.main(), 0)
        self.assertFalse(json.loads(output.getvalue())["binary_executed"])

    def test_posix_dispatch_replaces_process_with_verified_command_and_environment(self):
        command, child = launcher.launch_configuration(Path("/verified/mcp-grafana"),
                                                        {"SDS_GRAFANA_URL": "https://grafana.example", "SDS_GRAFANA_TOKEN": "token"})
        with mock.patch.object(launcher.os, "name", "posix"), mock.patch.object(launcher.os, "execve") as execute, \
                mock.patch.object(launcher.subprocess, "call") as fallback:
            launcher.execute(command, child)
        execute.assert_called_once_with(command[0], command, child)
        fallback.assert_not_called()

    def test_windows_dispatch_uses_same_explicit_command_and_environment(self):
        command, child = ["verified-mcp-grafana.exe", *launcher.FLAGS], {"DO_NOT_TRACK": "1"}
        with mock.patch.object(launcher.os, "name", "nt"), mock.patch.object(launcher.os, "execve") as execute, \
                mock.patch.object(launcher.subprocess, "call", return_value=0) as fallback:
            self.assertEqual(launcher.execute(command, child), 0)
        fallback.assert_called_once_with(command, env=child)
        execute.assert_not_called()

    def test_downloader_refuses_non_https_or_non_github_redirects(self):
        for url in ("http://github.com/a", "https://example.invalid/a", "https://user@github.com/a", "https://github.com:444/a"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                vendor.allowed_url(url)
        vendor.allowed_url("https://release-assets.githubusercontent.com/a?signature=synthetic")

    def test_downloader_is_bounded_atomic_and_checks_bytes(self):
        asset = self.asset()
        correct = (self.vendor_dir / asset["name"]).read_bytes()
        destination = self.root / "downloaded.tar.gz"
        for data in (correct[:-1], correct + b"extra", b"x" * len(correct), correct):
            with self.subTest(length=len(data), correct=data == correct):
                response = io.BytesIO(data)
                response.status, response.headers = 200, {}
                response.geturl = lambda: asset["url"]
                opener = mock.Mock()
                opener.open.return_value = response
                if data == correct:
                    vendor.download_one(asset, destination, opener)
                    self.assertEqual(destination.read_bytes(), correct)
                else:
                    with self.assertRaises(ValueError):
                        vendor.download_one(asset, destination, opener)
                    self.assertFalse(destination.exists())
                    self.assertEqual(list(self.root.glob(".grafana-download-*")), [])


if __name__ == "__main__":
    unittest.main()
