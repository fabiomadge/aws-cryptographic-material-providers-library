# Code generated by smithy-python-codegen DO NOT EDIT.

from Wrappers import Option_None, Option_Some
from _dafny import Map, Seq
import aws_cryptography_materialproviders.smithygenerated.models
import aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny
import module_
import software_amazon_cryptography_keystore_internaldafny
from software_amazon_cryptography_keystore_internaldafny_types import IKeyStoreClient
from software_amazon_cryptography_materialproviders_internaldafny_types import (
    AlgorithmSuiteId_DBE,
    AlgorithmSuiteId_ESDK,
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
    CacheType_Default,
    CacheType_MultiThreaded,
    CacheType_No,
    CacheType_SingleThreaded,
    CacheType_StormTracking,
    CommitmentPolicy_DBE,
    CommitmentPolicy_ESDK,
    CreateAwsKmsDiscoveryKeyringInput_CreateAwsKmsDiscoveryKeyringInput as DafnyCreateAwsKmsDiscoveryKeyringInput,
    CreateAwsKmsDiscoveryMultiKeyringInput_CreateAwsKmsDiscoveryMultiKeyringInput as DafnyCreateAwsKmsDiscoveryMultiKeyringInput,
    CreateAwsKmsHierarchicalKeyringInput_CreateAwsKmsHierarchicalKeyringInput as DafnyCreateAwsKmsHierarchicalKeyringInput,
    CreateAwsKmsKeyringInput_CreateAwsKmsKeyringInput as DafnyCreateAwsKmsKeyringInput,
    CreateAwsKmsMrkDiscoveryKeyringInput_CreateAwsKmsMrkDiscoveryKeyringInput as DafnyCreateAwsKmsMrkDiscoveryKeyringInput,
    CreateAwsKmsMrkDiscoveryMultiKeyringInput_CreateAwsKmsMrkDiscoveryMultiKeyringInput as DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput,
    CreateAwsKmsMrkKeyringInput_CreateAwsKmsMrkKeyringInput as DafnyCreateAwsKmsMrkKeyringInput,
    CreateAwsKmsMrkMultiKeyringInput_CreateAwsKmsMrkMultiKeyringInput as DafnyCreateAwsKmsMrkMultiKeyringInput,
    CreateAwsKmsMultiKeyringInput_CreateAwsKmsMultiKeyringInput as DafnyCreateAwsKmsMultiKeyringInput,
    CreateAwsKmsRsaKeyringInput_CreateAwsKmsRsaKeyringInput as DafnyCreateAwsKmsRsaKeyringInput,
    CreateCryptographicMaterialsCacheInput_CreateCryptographicMaterialsCacheInput as DafnyCreateCryptographicMaterialsCacheInput,
    CreateDefaultClientSupplierInput_CreateDefaultClientSupplierInput as DafnyCreateDefaultClientSupplierInput,
    CreateDefaultCryptographicMaterialsManagerInput_CreateDefaultCryptographicMaterialsManagerInput as DafnyCreateDefaultCryptographicMaterialsManagerInput,
    CreateMultiKeyringInput_CreateMultiKeyringInput as DafnyCreateMultiKeyringInput,
    CreateRawAesKeyringInput_CreateRawAesKeyringInput as DafnyCreateRawAesKeyringInput,
    CreateRawRsaKeyringInput_CreateRawRsaKeyringInput as DafnyCreateRawRsaKeyringInput,
    CreateRequiredEncryptionContextCMMInput_CreateRequiredEncryptionContextCMMInput as DafnyCreateRequiredEncryptionContextCMMInput,
    DecryptMaterialsInput_DecryptMaterialsInput as DafnyDecryptMaterialsInput,
    DecryptMaterialsOutput_DecryptMaterialsOutput as DafnyDecryptMaterialsOutput,
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    DeleteCacheEntryInput_DeleteCacheEntryInput as DafnyDeleteCacheEntryInput,
    DerivationAlgorithm_HKDF,
    DerivationAlgorithm_IDENTITY,
    DerivationAlgorithm_None,
    DiscoveryFilter_DiscoveryFilter as DafnyDiscoveryFilter,
    EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING,
    EdkWrappingAlgorithm_IntermediateKeyWrapping,
    Encrypt_AES__GCM,
    EncryptedDataKey_EncryptedDataKey as DafnyEncryptedDataKey,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    GetBranchKeyIdInput_GetBranchKeyIdInput as DafnyGetBranchKeyIdInput,
    GetBranchKeyIdOutput_GetBranchKeyIdOutput as DafnyGetBranchKeyIdOutput,
    GetCacheEntryInput_GetCacheEntryInput as DafnyGetCacheEntryInput,
    GetCacheEntryOutput_GetCacheEntryOutput as DafnyGetCacheEntryOutput,
    GetClientInput_GetClientInput as DafnyGetClientInput,
    GetEncryptionMaterialsInput_GetEncryptionMaterialsInput as DafnyGetEncryptionMaterialsInput,
    GetEncryptionMaterialsOutput_GetEncryptionMaterialsOutput as DafnyGetEncryptionMaterialsOutput,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    MaterialProvidersConfig_MaterialProvidersConfig as DafnyMaterialProvidersConfig,
    Materials_BeaconKey,
    Materials_BranchKey,
    Materials_Decryption,
    Materials_Encryption,
    OnDecryptInput_OnDecryptInput as DafnyOnDecryptInput,
    OnDecryptOutput_OnDecryptOutput as DafnyOnDecryptOutput,
    OnEncryptInput_OnEncryptInput as DafnyOnEncryptInput,
    OnEncryptOutput_OnEncryptOutput as DafnyOnEncryptOutput,
    PutCacheEntryInput_PutCacheEntryInput as DafnyPutCacheEntryInput,
    SignatureAlgorithm_ECDSA,
    SignatureAlgorithm_None,
    SymmetricSignatureAlgorithm_HMAC,
    SymmetricSignatureAlgorithm_None,
    UpdateUsageMetadataInput_UpdateUsageMetadataInput as DafnyUpdateUsageMetadataInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)
from software_amazon_cryptography_services_kms_internaldafny_types import IKMSClient


def SmithyToDafny_aws_cryptography_materialproviders_GetBranchKeyIdInput(input):
    return DafnyGetBranchKeyIdInput(
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetBranchKeyIdOutput(input):
    return DafnyGetBranchKeyIdOutput(
        branchKeyId=Seq(input.branch_key_id),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetClientInput(input):
    return DafnyGetClientInput(
        region=Seq(input.region),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetClientOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.client)

def SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input):
    import software_amazon_cryptography_services_kms_internaldafny
    client = software_amazon_cryptography_services_kms_internaldafny.default__.KMSClient()
    client.impl = input
    return client

def SmithyToDafny_aws_cryptography_materialproviders_PutCacheEntryInput(input):
    return DafnyPutCacheEntryInput(
        identifier=Seq(input.identifier),
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_Materials(input.materials),
        creationTime=input.creation_time,
        expiryTime=input.expiry_time,
        messagesUsed=((Option_Some(input.messages_used)) if (input.messages_used is not None) else (Option_None())),
        bytesUsed=((Option_Some(input.bytes_used)) if (input.bytes_used is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_Materials(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.MaterialsEncryption):
        Materials_union_value = Materials_Encryption(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.MaterialsDecryption):
        Materials_union_value = Materials_Decryption(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.MaterialsBranchKey):
        Materials_union_value = Materials_BranchKey(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.MaterialsBeaconKey):
        Materials_union_value = Materials_BeaconKey(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return Materials_union_value

def SmithyToDafny_smithy_api_Unit(input):
    return None

def SmithyToDafny_aws_cryptography_materialproviders_GetCacheEntryInput(input):
    return DafnyGetCacheEntryInput(
        identifier=Seq(input.identifier),
        bytesUsed=((Option_Some(input.bytes_used)) if (input.bytes_used is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetCacheEntryOutput(input):
    return DafnyGetCacheEntryOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_Materials(input.materials),
        creationTime=input.creation_time,
        expiryTime=input.expiry_time,
        messagesUsed=input.messages_used,
        bytesUsed=input.bytes_used,
    )

def SmithyToDafny_aws_cryptography_materialproviders_UpdateUsageMetadataInput(input):
    return DafnyUpdateUsageMetadataInput(
        identifier=Seq(input.identifier),
        bytesUsed=input.bytes_used,
    )

def SmithyToDafny_aws_cryptography_materialproviders_DeleteCacheEntryInput(input):
    return DafnyDeleteCacheEntryInput(
        identifier=Seq(input.identifier),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetEncryptionMaterialsInput(input):
    return DafnyGetEncryptionMaterialsInput(
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        commitmentPolicy=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CommitmentPolicy(input.commitment_policy),
        algorithmSuiteId=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm_suite_id))) if (input.algorithm_suite_id is not None) else (Option_None())),
        maxPlaintextLength=((Option_Some(input.max_plaintext_length)) if (input.max_plaintext_length is not None) else (Option_None())),
        requiredEncryptionContextKeys=((Option_Some(Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]))) if (input.required_encryption_context_keys is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CommitmentPolicy(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CommitmentPolicyESDK):
        CommitmentPolicy_union_value = CommitmentPolicy_ESDK(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CommitmentPolicyDBE):
        CommitmentPolicy_union_value = CommitmentPolicy_DBE(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return CommitmentPolicy_union_value

def SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.AlgorithmSuiteIdESDK):
        AlgorithmSuiteId_union_value = AlgorithmSuiteId_ESDK(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.AlgorithmSuiteIdDBE):
        AlgorithmSuiteId_union_value = AlgorithmSuiteId_DBE(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return AlgorithmSuiteId_union_value

def SmithyToDafny_aws_cryptography_materialproviders_GetEncryptionMaterialsOutput(input):
    return DafnyGetEncryptionMaterialsOutput(
        encryptionMaterials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input.encryption_materials),
    )

def SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input):
    return DafnyEncryptionMaterials(
        algorithmSuite=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input.algorithm_suite),
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        encryptedDataKeys=Seq([aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encrypted_data_keys]),
        requiredEncryptionContextKeys=Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]),
        plaintextDataKey=((Option_Some(Seq(input.plaintext_data_key))) if (input.plaintext_data_key is not None) else (Option_None())),
        signingKey=((Option_Some(Seq(input.signing_key))) if (input.signing_key is not None) else (Option_None())),
        symmetricSigningKeys=((Option_Some(Seq([Seq(list_element) for list_element in input.symmetric_signing_keys]))) if (input.symmetric_signing_keys is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input):
    return DafnyAlgorithmSuiteInfo(
        id=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.id),
        binaryId=Seq(input.binary_id),
        messageVersion=input.message_version,
        encrypt=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_Encrypt(input.encrypt),
        kdf=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DerivationAlgorithm(input.kdf),
        commitment=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DerivationAlgorithm(input.commitment),
        signature=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_SignatureAlgorithm(input.signature),
        symmetricSignature=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(input.symmetric_signature),
        edkWrapping=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EdkWrappingAlgorithm(input.edk_wrapping),
    )

def SmithyToDafny_aws_cryptography_materialproviders_EncryptedDataKey(input):
    return DafnyEncryptedDataKey(
        keyProviderId=Seq(input.key_provider_id),
        keyProviderInfo=Seq(input.key_provider_info),
        ciphertext=Seq(input.ciphertext),
    )

def SmithyToDafny_aws_cryptography_materialproviders_Encrypt(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.EncryptAES_GCM):
        Encrypt_union_value = Encrypt_AES__GCM(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return Encrypt_union_value

def SmithyToDafny_aws_cryptography_materialproviders_DerivationAlgorithm(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmHKDF):
        DerivationAlgorithm_union_value = DerivationAlgorithm_HKDF(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmIDENTITY):
        DerivationAlgorithm_union_value = DerivationAlgorithm_IDENTITY(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.DerivationAlgorithmNone):
        DerivationAlgorithm_union_value = DerivationAlgorithm_None(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return DerivationAlgorithm_union_value

def SmithyToDafny_aws_cryptography_materialproviders_SignatureAlgorithm(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.SignatureAlgorithmECDSA):
        SignatureAlgorithm_union_value = SignatureAlgorithm_ECDSA(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.SignatureAlgorithmNone):
        SignatureAlgorithm_union_value = SignatureAlgorithm_None(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return SignatureAlgorithm_union_value

def SmithyToDafny_aws_cryptography_materialproviders_SymmetricSignatureAlgorithm(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.SymmetricSignatureAlgorithmHMAC):
        SymmetricSignatureAlgorithm_union_value = SymmetricSignatureAlgorithm_HMAC(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.SymmetricSignatureAlgorithmNone):
        SymmetricSignatureAlgorithm_union_value = SymmetricSignatureAlgorithm_None(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return SymmetricSignatureAlgorithm_union_value

def SmithyToDafny_aws_cryptography_materialproviders_EdkWrappingAlgorithm(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.EdkWrappingAlgorithmDIRECT_KEY_WRAPPING):
        EdkWrappingAlgorithm_union_value = EdkWrappingAlgorithm_DIRECT__KEY__WRAPPING(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.EdkWrappingAlgorithmIntermediateKeyWrapping):
        EdkWrappingAlgorithm_union_value = EdkWrappingAlgorithm_IntermediateKeyWrapping(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return EdkWrappingAlgorithm_union_value

def SmithyToDafny_aws_cryptography_materialproviders_DecryptMaterialsInput(input):
    return DafnyDecryptMaterialsInput(
        algorithmSuiteId=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm_suite_id),
        commitmentPolicy=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CommitmentPolicy(input.commitment_policy),
        encryptedDataKeys=Seq([aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encrypted_data_keys]),
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        reproducedEncryptionContext=((Option_Some(Map({Seq(key): Seq(value) for (key, value) in input.reproduced_encryption_context.items() }))) if (input.reproduced_encryption_context is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_DecryptMaterialsOutput(input):
    return DafnyDecryptMaterialsOutput(
        decryptionMaterials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input.decryption_materials),
    )

def SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input):
    return DafnyDecryptionMaterials(
        algorithmSuite=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input.algorithm_suite),
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        requiredEncryptionContextKeys=Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]),
        plaintextDataKey=((Option_Some(Seq(input.plaintext_data_key))) if (input.plaintext_data_key is not None) else (Option_None())),
        verificationKey=((Option_Some(Seq(input.verification_key))) if (input.verification_key is not None) else (Option_None())),
        symmetricSigningKey=((Option_Some(Seq(input.symmetric_signing_key))) if (input.symmetric_signing_key is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_OnEncryptInput(input):
    return DafnyOnEncryptInput(
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input.materials),
    )

def SmithyToDafny_aws_cryptography_materialproviders_OnEncryptOutput(input):
    return DafnyOnEncryptOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input.materials),
    )

def SmithyToDafny_aws_cryptography_materialproviders_OnDecryptInput(input):
    return DafnyOnDecryptInput(
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input.materials),
        encryptedDataKeys=Seq([aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptedDataKey(list_element) for list_element in input.encrypted_data_keys]),
    )

def SmithyToDafny_aws_cryptography_materialproviders_OnDecryptOutput(input):
    return DafnyOnDecryptOutput(
        materials=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input.materials),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(input):
    return DafnyCreateAwsKmsDiscoveryKeyringInput(
        kmsClient=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.kms_client),
        discoveryFilter=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DiscoveryFilter(input.discovery_filter))) if (input.discovery_filter is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_DiscoveryFilter(input):
    return DafnyDiscoveryFilter(
        accountIds=Seq([Seq(list_element) for list_element in input.account_ids]),
        partition=Seq(input.partition),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateMultiKeyringInput(input):
    return DafnyCreateMultiKeyringInput(
        generator=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(input.generator))) if (input.generator is not None) else (Option_None())),
        childKeyrings=Seq([aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(list_element) for list_element in input.child_keyrings]),
    )

def SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(input):
    return input._impl

def SmithyToDafny_aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(input):
    return DafnyValidEncryptionMaterialsTransitionInput(
        start=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input.start),
        stop=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(input.stop),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(input):
    return DafnyCreateDefaultCryptographicMaterialsManagerInput(
        keyring=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(input.keyring),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateRawRsaKeyringInput(input):
    return DafnyCreateRawRsaKeyringInput(
        keyNamespace=Seq(input.key_namespace),
        keyName=Seq(input.key_name),
        paddingScheme=input.padding_scheme,
        publicKey=((Option_Some(Seq(input.public_key))) if (input.public_key is not None) else (Option_None())),
        privateKey=((Option_Some(Seq(input.private_key))) if (input.private_key is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(input):
    return DafnyInitializeEncryptionMaterialsInput(
        algorithmSuiteId=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm_suite_id),
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        requiredEncryptionContextKeys=Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]),
        signingKey=((Option_Some(Seq(input.signing_key))) if (input.signing_key is not None) else (Option_None())),
        verificationKey=((Option_Some(Seq(input.verification_key))) if (input.verification_key is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(input):
    return DafnyCreateAwsKmsMultiKeyringInput(
        generator=((Option_Some(Seq(input.generator))) if (input.generator is not None) else (Option_None())),
        kmsKeyIds=((Option_Some(Seq([Seq(list_element) for list_element in input.kms_key_ids]))) if (input.kms_key_ids is not None) else (Option_None())),
        clientSupplier=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input.client_supplier))) if (input.client_supplier is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input):
    return input._impl

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(input):
    return DafnyCreateAwsKmsMrkDiscoveryKeyringInput(
        kmsClient=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.kms_client),
        discoveryFilter=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DiscoveryFilter(input.discovery_filter))) if (input.discovery_filter is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
        region=Seq(input.region),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(input):
    return DafnyCreateAwsKmsHierarchicalKeyringInput(
        branchKeyId=((Option_Some(Seq(input.branch_key_id))) if (input.branch_key_id is not None) else (Option_None())),
        branchKeyIdSupplier=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_BranchKeyIdSupplierReference(input.branch_key_id_supplier))) if (input.branch_key_id_supplier is not None) else (Option_None())),
        keyStore=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyStoreReference(input.key_store),
        ttlSeconds=input.ttl_seconds,
        cache=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CacheType(input.cache))) if (input.cache is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_BranchKeyIdSupplierReference(input):
    return input._impl

def SmithyToDafny_aws_cryptography_materialproviders_KeyStoreReference(input):
    return input._config.dafnyImplInterface.impl
    # import aws_cryptography_keystore.smithygenerated.config
    # aws_cryptography_keystore_client = software_amazon_cryptography_keystore_internaldafny.KeyStoreClient()
    # aws_cryptography_keystore_client.ctor__(aws_cryptography_keystore.smithygenerated.config.smithy_config_to_dafny_config(input._config))
    # return aws_cryptography_keystore_client

def SmithyToDafny_aws_cryptography_materialproviders_CacheType(input):
    if isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CacheTypeDefault):
        CacheType_union_value = CacheType_Default(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CacheTypeNo):
        CacheType_union_value = CacheType_No(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CacheTypeSingleThreaded):
        CacheType_union_value = CacheType_SingleThreaded(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CacheTypeMultiThreaded):
        CacheType_union_value = CacheType_MultiThreaded(input.value)
    elif isinstance(input, aws_cryptography_materialproviders.smithygenerated.models.CacheTypeStormTracking):
        CacheType_union_value = CacheType_StormTracking(input.value)
    else:
        raise ValueError("No recognized union value in union type: " + input)

    return CacheType_union_value

def SmithyToDafny_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(input):
    return DafnyValidateCommitmentPolicyOnDecryptInput(
        algorithm=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm),
        commitmentPolicy=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CommitmentPolicy(input.commitment_policy),
    )

def SmithyToDafny_aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(input):
    return DafnyValidDecryptionMaterialsTransitionInput(
        start=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input.start),
        stop=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(input.stop),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(input):
    return DafnyCreateAwsKmsMrkDiscoveryMultiKeyringInput(
        regions=Seq([Seq(list_element) for list_element in input.regions]),
        discoveryFilter=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DiscoveryFilter(input.discovery_filter))) if (input.discovery_filter is not None) else (Option_None())),
        clientSupplier=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input.client_supplier))) if (input.client_supplier is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(input):
    return DafnyCreateAwsKmsKeyringInput(
        kmsKeyId=Seq(input.kms_key_id),
        kmsClient=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.kms_client),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateRawAesKeyringInput(input):
    return DafnyCreateRawAesKeyringInput(
        keyNamespace=Seq(input.key_namespace),
        keyName=Seq(input.key_name),
        wrappingKey=Seq(input.wrapping_key),
        wrappingAlg=input.wrapping_alg,
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(input):
    return DafnyCreateRequiredEncryptionContextCMMInput(
        underlyingCMM=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input.underlying_cmm))) if (input.underlying_cmm is not None) else (Option_None())),
        keyring=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(input.keyring))) if (input.keyring is not None) else (Option_None())),
        requiredEncryptionContextKeys=Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input):
    return input._impl

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(input):
    return DafnyCreateAwsKmsRsaKeyringInput(
        publicKey=((Option_Some(Seq(input.public_key))) if (input.public_key is not None) else (Option_None())),
        kmsKeyId=Seq(input.kms_key_id),
        encryptionAlgorithm=Seq(input.encryption_algorithm),
        kmsClient=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.kms_client))) if (input.kms_client is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(input):
    return DafnyCreateCryptographicMaterialsCacheInput(
        cache=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CacheType(input.cache),
    )

def SmithyToDafny_aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(input):
    return DafnyInitializeDecryptionMaterialsInput(
        algorithmSuiteId=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm_suite_id),
        encryptionContext=Map({Seq(key): Seq(value) for (key, value) in input.encryption_context.items() }),
        requiredEncryptionContextKeys=Seq([Seq(list_element) for list_element in input.required_encryption_context_keys]),
    )

def SmithyToDafny_aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(input):
    return Seq(input.binary_id)

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(input):
    return DafnyCreateAwsKmsDiscoveryMultiKeyringInput(
        regions=Seq([Seq(list_element) for list_element in input.regions]),
        discoveryFilter=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DiscoveryFilter(input.discovery_filter))) if (input.discovery_filter is not None) else (Option_None())),
        clientSupplier=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input.client_supplier))) if (input.client_supplier is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(input):
    return DafnyCreateAwsKmsMrkKeyringInput(
        kmsKeyId=Seq(input.kms_key_id),
        kmsClient=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KmsClientReference(input.kms_client),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(input):
    return DafnyValidateCommitmentPolicyOnEncryptInput(
        algorithm=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteId(input.algorithm),
        commitmentPolicy=aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CommitmentPolicy(input.commitment_policy),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(input):
    return DafnyCreateAwsKmsMrkMultiKeyringInput(
        generator=((Option_Some(Seq(input.generator))) if (input.generator is not None) else (Option_None())),
        kmsKeyIds=((Option_Some(Seq([Seq(list_element) for list_element in input.kms_key_ids]))) if (input.kms_key_ids is not None) else (Option_None())),
        clientSupplier=((Option_Some(aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input.client_supplier))) if (input.client_supplier is not None) else (Option_None())),
        grantTokens=((Option_Some(Seq([Seq(list_element) for list_element in input.grant_tokens]))) if (input.grant_tokens is not None) else (Option_None())),
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(input):
    return DafnyCreateDefaultClientSupplierInput(
    )

def SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_KeyringReference(input.keyring)

def SmithyToDafny_aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input.materials_manager)

def SmithyToDafny_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsManagerReference(input.materials_manager)

def SmithyToDafny_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(input.materials_cache)

def SmithyToDafny_aws_cryptography_materialproviders_CryptographicMaterialsCacheReference(input):
    return input._impl

def SmithyToDafny_aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(input):
    return aws_cryptography_materialproviders.smithygenerated.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_ClientSupplierReference(input.client)

def SmithyToDafny_aws_cryptography_materialproviders_MaterialProvidersConfig(input):
    return DafnyMaterialProvidersConfig(
    )
