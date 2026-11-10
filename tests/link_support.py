"""Create link fixtures, skipping only when this filesystem denies them."""
import errno
import os
from pathlib import Path


def _unsupported(test, kind, error):
    if (isinstance(error, PermissionError)
            or getattr(error, "winerror", None) in {5, 1314}
            or error.errno in {errno.EPERM, errno.EACCES, errno.ENOSYS, errno.EOPNOTSUPP}):
        test.skipTest(kind + " creation is unavailable in this test environment: " + str(error))
    raise error


def create_symlink_or_skip(test, link, target, target_is_directory=False):
    try:
        Path(link).symlink_to(target, target_is_directory=target_is_directory)
    except OSError as error:
        _unsupported(test, "Symbolic-link fixture", error)


def create_hardlink_or_skip(test, link, target):
    try:
        os.link(target, link)
    except OSError as error:
        _unsupported(test, "Hard-link fixture", error)
