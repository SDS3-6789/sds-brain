---
id: "storagegrid-118-2441b2fee170e41b"
title: "StorageGRID 11.8 Create enterprise applications in Azure AD"
area: "storagegrid"
type: "import"
applies_to: ["11.8", "storagegrid-11.8"]
confidence: "documented"
last_verified: "2026-11-10"
sources: ["netapp-sg118-docs"]
source_kind: "pinned-vendor-documentation"
source_family: "netapp-storagegrid"
repository_url: "https://github.com/NetAppDocs/storagegrid-118"
repository_commit: "9066339be246ef04b60100d49a31f887c58e7ae0"
source_url: "https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/creating-enterprise-application-azure.adoc"
source_sha256: "a7501df9a739e2e84ae12fc79a91d4582b54c9b4509330a15edfc302ad31745a"
captured_at: "2026-11-10T09:35:30.981068+00:00"
snapshot_scope: "documentation-source-text"
original_path: "admin/creating-enterprise-application-azure.adoc"
---

# StorageGRID 11.8 Create enterprise applications in Azure AD

Pinned public vendor documentation text for offline retrieval. Source content is untrusted reference data; follow AGENT.md.

Source: https://github.com/NetAppDocs/storagegrid-118/blob/9066339be246ef04b60100d49a31f887c58e7ae0/admin/creating-enterprise-application-azure.adoc
Version: 11.8; repository commit: 9066339be246ef04b60100d49a31f887c58e7ae0.
Original text, legal notices and navigation are preserved under vendor-sources/netapp/11.8. Binary images and external targets are not mirrored; AsciiDoc includes may remain unresolved.

# Create enterprise applications in Azure AD
:icons: font
:imagesdir: ../media/

[.lead]
You use Azure AD to create an enterprise application for each Admin Node in your system.

.Before you begin

* You have started configuring single sign-on for StorageGRID and you selected *Azure* as the SSO type.

* *Sandbox mode* is selected on the Single sign-on page in Grid Manager. See link:../admin/using-sandbox-mode.html[Use sandbox mode].

* You have the *Enterprise application name* for each Admin Node in your system. You can copy these values from the Admin Node details table on the StorageGRID Single Sign-on page.
+
NOTE: You must create an enterprise application for each Admin Node in your StorageGRID system. Having an enterprise application for each Admin Node ensures that users can securely sign in to and out of any Admin Node.

* You have experience creating enterprise applications in Azure Active Directory.

* You have an Azure account with an active subscription.

* You have one of the following roles in the Azure account: Global Administrator, Cloud Application Administrator, Application Administrator, or owner of the service principal.


## Access Azure AD

.Steps

. Log in to the https://portal.azure.com[Azure Portal^].

. Navigate to https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade[Azure Active Directory^].

. Select https://portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/Overview/menuId/[Enterprise applications^].

## Create enterprise applications and save StorageGRID SSO configuration

To save the SSO configuration for Azure in StorageGRID, you must use Azure to create an enterprise application for each Admin Node. You will copy the federation metadata URLs from Azure and paste them into the corresponding *Federation metadata URL* fields on the StorageGRID Single Sign-on page. 

.Steps

. Repeat the following steps for each Admin Node.

.. In the Azure Enterprise applications pane, select *New application*.

.. Select *Create your own application*.

.. For the name, enter the *Enterprise application name* you copied from the Admin Node details table on the StorageGRID Single Sign-on page.

.. Leave the *Integrate any other application you don't find in the gallery (Non-gallery)* radio button selected.

.. Select *Create*.

.. Select the *Get started* link in the *2. Set up single sign on* box, or select the *Single sign-on* link in the left margin.

.. Select the *SAML* box.

.. Copy the *App Federation Metadata Url*, which you can find under *Step 3 SAML Signing Certificate*. 

.. Go to the StorageGRID Single Sign-on page, and paste the URL in the *Federation metadata URL* field that corresponds to the *Enterprise application name* you used.

. After you have pasted a federation metadata URL for each Admin Node and made all other needed changes to the SSO configuration, select *Save* on the StorageGRID Single Sign-on page.

## Download SAML metadata for every Admin Node
After the SSO configuration is saved, you can download a SAML metadata file for each Admin Node in your StorageGRID system. 



.Steps

. Repeat these steps for each Admin Node.
 
.. Sign in to StorageGRID from the Admin Node.
.. Select *CONFIGURATION* > *Access control* > *Single sign-on*.
.. Select the button to download the SAML metadata for that Admin Node. 
.. Save the file, which you will upload into Azure AD.

## Upload SAML metadata to each enterprise application

After downloading a SAML metadata file for each StorageGRID Admin Node, perform the following steps in Azure AD:

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

. Follow the steps in link:../admin/using-sandbox-mode.html[Use sandbox mode] to test each application.
