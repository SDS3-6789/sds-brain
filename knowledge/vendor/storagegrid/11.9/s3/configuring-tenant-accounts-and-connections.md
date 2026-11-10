---
id: "storagegrid-119-acfdf4a4aa77103e"
title: "StorageGRID 11.9 Test S3 REST API configuration"
area: "storagegrid"
type: "import"
applies_to: ["11.9", "storagegrid-11.9"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg119-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-119"
repository_commit: "aa58c9affae3bb1994d6bd2e525851e3fd088517"
source_url: "https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/configuring-tenant-accounts-and-connections.adoc"
source_sha256: "f02312cb97b1f6593576e29cdf10b235d01762d2538079ba143bb7dd0b6cbffc"
captured_at: "2026-11-10T09:31:11.169093+00:00"
snapshot_scope: "documentation-source-text"
original_path: "s3/configuring-tenant-accounts-and-connections.adoc"
---

# StorageGRID 11.9 Test S3 REST API configuration

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-119/blob/aa58c9affae3bb1994d6bd2e525851e3fd088517/s3/configuring-tenant-accounts-and-connections.adoc
Version: 11.9; repository commit: aa58c9affae3bb1994d6bd2e525851e3fd088517.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.9. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Test S3 REST API configuration
:icons: font
:imagesdir: ../media/

[.lead]
You can use the Amazon Web Services Command Line Interface (AWS CLI) to test your connection to the system and to verify that you can read and write objects.

.Before you begin
* You have downloaded and installed the AWS CLI from https://aws.amazon.com/cli[aws.amazon.com/cli^].
* Optionally, you have link:../admin/configuring-load-balancer-endpoints.html[created a load balancer endpoint]. Otherwise, you know the IP address of the Storage Node you want to connect to and the port number to use. See link:../admin/summary-ip-addresses-and-ports-for-client-connections.html[IP addresses and ports for client connections].
* You have link:../admin/creating-tenant-account.html[created an S3 tenant account].
* You have signed in to the tenant and link:../tenant/creating-your-own-s3-access-keys.html[created an access key].

For details on these steps, see link:../admin/configuring-client-connections.html[Configure client connections].

.Steps
. Configure the AWS CLI settings to use the account you created in the StorageGRID system:
 .. Enter configuration mode: `aws configure`
 .. Enter the access key ID for the account you created.
 .. Enter the secret access key for the account you created.
 .. Enter the default region to use. For example, `us-east-1`.
 .. Enter the default output format to use, or press *Enter* to select JSON.
. Create a bucket.
+
This example assumes you configured a load balancer endpoint to use IP address 10.96.101.17 and port 10443.
+
----
aws s3api --endpoint-url https://10.96.101.17:10443
--no-verify-ssl create-bucket --bucket testbucket
----
+
If the bucket is created successfully, the location of the bucket is returned, as seen in the following example:
+
----
"Location": "/testbucket"
----

. Upload an object.
+
----
aws s3api --endpoint-url https://10.96.101.17:10443 --no-verify-ssl
put-object --bucket testbucket --key s3.pdf --body C:\s3-test\upload\s3.pdf
----
+
If the object is uploaded successfully, an Etag is returned which is a hash of the object data.

. List the contents of the bucket to verify that the object was uploaded.
+
----
aws s3api --endpoint-url https://10.96.101.17:10443 --no-verify-ssl
list-objects --bucket testbucket
----

. Delete the object.
+
----
aws s3api --endpoint-url https://10.96.101.17:10443 --no-verify-ssl
delete-object --bucket testbucket --key s3.pdf
----

. Delete the bucket.
+
----
aws s3api --endpoint-url https://10.96.101.17:10443 --no-verify-ssl
delete-bucket --bucket testbucket
----
