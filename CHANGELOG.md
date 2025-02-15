# Changelog

# [1.4.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.3.0...v1.4.0) (2024-05-20)

### Features

- **Keystore:** Introduce additional KMSConfiguration options ([#316](https://github.com/aws/aws-cryptographic-material-providers-library/issues/316)) ([f3a0a52](https://github.com/aws/aws-cryptographic-material-providers-library/commit/f3a0a5269e611afd254425226d32eaaed1f3d99b))

The Hierarchical Keyring's Keystore now supports four (4) `KMSConfigurations`:

- kmsKeyArn
- kmsMRKeyArn
- discovery
- mrDiscovery

See our [JavaDocs](https://aws.github.io/aws-cryptographic-material-providers-library/index.html?software/amazon/cryptography/keystore/model/KMSConfiguration.html) for details
on how these options effect the relationship between
a Keystore and KMS.

### Maintenance

- .NET : Bump dependency [BouncyCastle.Cryptography](https://github.com/bcgit/bc-csharp) from 2.2.1 to 2.3.1. ([#329](https://github.com/aws/aws-cryptographic-material-providers-library/pull/329))
- .NET : Bump dependency [AWSSDK.Core](https://github.com/aws/aws-sdk-net) from 3.7.300.2 to 3.7.304.2. ([#329](https://github.com/aws/aws-cryptographic-material-providers-library/pull/329))
- Java : Move InternalResult into StandardLibrary(Internal) ([#325](https://github.com/aws/aws-cryptographic-material-providers-library/pull/325))

# [1.3.0](https://github.com/aws/aws-cryptographic-material-providers-library/compare/v1.2.0...v1.3.0) (2024-04-24)

### Bug Fixes

- **dafny:** Local Service Constructors MUST return concrete ([64f72c1](https://github.com/aws/aws-cryptographic-material-providers-library/commit/64f72c121fef31a83bcf3a5346d7efc1e84ab25f))
- Improvements to the Java Release process ([#162](https://github.com/aws/aws-cryptographic-material-providers-library/issues/162)) ([d92c06a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d92c06a2fd355290f27df669c866157e14da9793))
- Increase try-block scope when calling MPL components ([#267](https://github.com/aws/aws-cryptographic-material-providers-library/issues/267)) ([7661bf4](https://github.com/aws/aws-cryptographic-material-providers-library/commit/7661bf4b0f23e810f825fd884ecdc036b5e472d5))

### Features

- Multi-Region Key Logic in the Keystore ([#285](https://github.com/aws/aws-cryptographic-material-providers-library/issues/285)) ([d924395](https://github.com/aws/aws-cryptographic-material-providers-library/commit/d924395e7895187aee59279f7ba1f4dcdf1f893e))
- .NET : Enforce User input Constraints at Type Conversion ([#281](https://github.com/aws/aws-cryptographic-material-providers-library/issues/281)) ([04102d7](https://github.com/aws/aws-cryptographic-material-providers-library/commit/04102d7e30c04167df9fb76de86d2aeb0508536e))
- Update error message to include expected values when no Encrypted Data Keys found to match ([#275](https://github.com/aws/aws-cryptographic-material-providers-library/issues/275)) ([da95f9a](https://github.com/aws/aws-cryptographic-material-providers-library/commit/da95f9a66f863016f8172df9aa19d1086b9bdd78))

## 1.2.0 (2024-01-08)

### Features

    * add command line parser (#131)

### Bug Fixes

    * resolve awssdk:core dependency in TestVectors build.gradle.kts (#177)
    * add more tests to ComputeSetToOrderedSequence (#111)
    * Empty string defers to SDK default region (#127)
    * update mpl .csproj to use project references (#134)
    * newest polymorph for newest shims. Catch all exceptions. DDB only (#135)
    * update README for repo rename update (#147)
    * rerun latest polymorph. (#128)
    * typo lead to two verification, no format (#130)
    * Improve compatibility with Dafny 4.4 (#129)

### Maintenance

    * A variety of fixes to the libraries CI and testing

## 1.0.2 (2023-10-18)

### Bug Fixes

    * CmpError must return custom error message (#118) (86abacc)
    * Deafult entryPruningTailSize (#93) (0344e9f)
    * Fix brittle concurrent test (#105) (#60) (c043162)
    * fix typo in encryption materials validation (cd6b0aa), closes #84
    * fix typo in encryption materials validation (89a234c)
    * Forward the underlying error (#90) (bc21551)

## 1.0.1 2023-07-26

### Fix

- Fixes a runtime check in `VersionKey` Key Store API that no longer checks for the CipherText length
  on the output of a KMS ReEncrypt API call.

## 1.0.0 2023-07-21

### Features

- Introduces Thread Safe Cryptographic Materials Caches (CMCs):
  - Storm Tracking Cache  
    Safe for use in a multi threaded environment,  
    tries to prevent redundant or overly parallel backend calls.  
    See [Spec changes](https://github.com/awslabs/aws-encryption-sdk-specification/blob/ce9a4062124edc5085c66a4f10742e15aa039b34/changes/2023-06-19_thread_safe_cache/change.md) for details.
  - Multi Threaded Cache  
    Safe for use in a multi threaded environment,  
    but no extra functionality

### BREAKING CHANGES

- CMCs:
  - Original Cryptographic Materials Cache has been renamed to Single Threaded Cache
  - `CreateCryptographicMaterialsCacheInput` now ONLY accepts `CacheType`,  
    which determines which, if any, of the three implemented CMCs will be returned.
  - The `DefaultCache` is `StormTrackingCache`
- `CreateAwsKmsHierarchicalKeyringInput`:
  - no longer has a `maxCacheSize` field
  - now has an optional `cache` field for a `CacheType`
- Hierarchical Keyring's Key Store:
  - The Hierarchical Keyring's Key Store's Data Structure has changed.  
    As such, entries persisted in the Key Store with prior versions of this library are NOT compatibale.  
    Instead, we recommend Creating a new DynamoDB Table for this version of the Key Store.
  - The Key Store's `CreateKeyInput` now takes:
    - An Optional `String branchKeyIdentifier`
    - An Optional `EncryptionContext encryptionContext`
      - This `encryptionContext` will be added to the Encryption Context sent to KMS prefixed with `aws-crypto-ec:`
  - Creating a Key now also calls KMS:ReEncrypt
  - `CreateKeyStore` no longer creates a GSI
  - The Encryption Context used with KMS' `GenerateDataKeyWithoutPlaintext` no longer include's the discarded GSI's `status`.
  - More details about the Key Store's changes are avaible in our Specification:
    - [2023-07-12 Update Key Store](https://github.com/awslabs/aws-encryption-sdk-specification/tree/master/changes/2023_7_12_update-keystore-structure)
    - [KeyStore Specification](https://github.com/awslabs/aws-encryption-sdk-specification/blob/master/framework/branch-key-store.md)

### Maintenance

- A variety of fixes to the libraries CI and testing

### Fix

- Fixes Required Encryption Context CMM and UpdateUsageMetadata names in smithy model

## 1.0.0-preview-3 2023-06-22

### Fix

- Fixes PutCacheEntry
  - PutCacheEntry will now update an entry.
    This simplifies using the cache in concurrent situations.
    Rather than having the caller implement some retry logic
    the cache will now update the entry.
- Fixes pom.xml to include runtime version of BouncyCastle and removes bundling of BC in the jar.

## 1.0.0-preview-2 2023-06-19

### Fix

- Fixes build file to correctly generate pom file with correct dependencies during release.

## 1.0.0-preview-1 2023-06-07

### Features

- Initial release of the AWS Cryptographic Material Providers Library.
  This release is considered a [developer preview](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle)
  and is not intended for production use cases.
