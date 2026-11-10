---
id: "storagegrid-120-6f982062b94d785e"
title: "StorageGRID 12.0 Create enterprise applications in Entra ID for StorageGRID"
area: "storagegrid"
type: "import"
applies_to: ["12.0", "storagegrid-12.0"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg120-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-120"
repository_commit: "92a3f4cb2ac43fd5f151e410f99e7b9d4b019938"
source_url: "https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/creating-enterprise-application-entra-id.adoc"
source_sha256: "75c8df9abdaa00e5a43b98ee4ee3fde05abb7111e212051b770b98d9ca2df4d9"
captured_at: "2026-11-10T09:31:38.190992+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/creating-enterprise-application-entra-id.adoc"
---

# StorageGRID 12.0 Create enterprise applications in Entra ID for StorageGRID

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-120/blob/92a3f4cb2ac43fd5f151e410f99e7b9d4b019938/admin/creating-enterprise-application-entra-id.adoc
Version: 12.0; repository commit: 92a3f4cb2ac43fd5f151e410f99e7b9d4b019938.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/12.0. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create enterprise applications in Entra ID for StorageGRID
:icons: font
:imagesdir: ../media/

[.lead]
You use Entra ID to create an enterprise application for each Admin Node in your system.

.Before you begin

* You have started configuring single sign-on for StorageGRID and you selected *Entra ID* as the SSO type.

* You have link:../admin/configure-sso.html#enter-sandbox-mode[entered sandbox mode] in Grid Manager.

* You have the *Enterprise application name* for each Admin Node in your system. You can copy these values from the Admin Node details table on the Configure SSO page.
+
NOTE: You must create an enterprise application for each Admin Node in your StorageGRID system. Having an enterprise application for each Admin Node ensures that users can securely sign in to and out of any Admin Node.

* You have experience creating enterprise applications in Entra ID.

* You have an Entra ID account with an active subscription.

* You have one of the following roles in the Entra ID account: Global Administrator, Cloud Application Administrator, Application Administrator, or owner of the service principal.

## Access Entra ID

.Steps

. Log in to the https://portal.azure.com[Azure Portal^].

. Navigate to https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade[Entra ID^].

. Select https://portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/Overview/menuId/[Enterprise applications^].

## Create enterprise applications and save StorageGRID SSO configuration

To save the SSO configuration for Entra ID in StorageGRID, you must use Entra ID to create an enterprise application for each Admin Node. You will copy the federation metadata URLs from Entra ID and paste them into the corresponding *Federation metadata URL* fields on the Configure SSO page. 

.Steps

. Repeat the following steps for each Admin Node.

.. In the Entra ID Enterprise applications pane, select *New application*.

.. Select *Create your own application*.

.. For the name, enter the *Enterprise application name* you copied from the Admin Node details table on the Configure SSO page.

.. Leave the *Integrate any other application you don't find in the gallery (Non-gallery)* radio button selected.

.. Select *Create*.

.. Select the *Get started* link in the *2. Set up single sign on* box, or select the *Single sign-on* link in the left margin.

.. Select the *SAML* box.

.. Copy the *App Federation Metadata Url*, which you can find under *Step 3 SAML Signing Certificate*. 

.. Go to the Configure SSO page, and paste the URL in the *Federation metadata URL* field that corresponds to the *Enterprise application name* you used.

. After you have pasted a federation metadata URL for each Admin Node and made all other needed changes to the SSO configuration, select *Save* on the Configure SSO page.

## Download SAML metadata for every Admin Node
After the SSO configuration is saved, you can download a SAML metadata file for each Admin Node in your StorageGRID system. 

.Steps

. Repeat these steps for each Admin Node.
 
.. Sign in to StorageGRID from the Admin Node.
.. Select *Configuration* > *Access control* > *Single sign-on*.
.. Select the button to download the SAML metadata for that Admin Node. 
.. Save the file, which you will upload into Entra ID.

## Upload SAML metadata to each enterprise application

After downloading a SAML metadata file for each StorageGRID Admin Node, perform the following steps in Entra ID:

.Steps

. Return to the Azure Portal.
. Repeat these steps for each enterprise application:
+
NOTE: You might need to refresh the Enterprise applications page to see applications you previously added in the list.

.. Go to the Properties page for the enterprise application.
.. Set *Assignment required* to *No* (unless you want to separately configure assignments).
.. Go to the Single sign-on page.
.. Complete the SAML configuration.
.. Select the *Upload metadata file* button and select the SAML metadata file you downloaded for the corresponding Admin Node. 
.. After the file loads, select *Save* and then select *X* to close the pane. You are returned to the Set up Single Sign-On with SAML page. 

. link:../admin/configure-sso.html#test-sso[Test each application].

// 2025 JUN 10, SGWS-33778
