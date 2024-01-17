# Code generated by smithy-python-codegen DO NOT EDIT.

import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.models
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny
import module_
from null.smithygenerated.aws_cryptography_keystore.shim import (
    smithy_error_to_dafny_error as aws_cryptography_keystore_smithy_error_to_dafny_error,
)
from null.smithygenerated.aws_cryptography_primitives.shim import (
    smithy_error_to_dafny_error as aws_cryptography_primitives_smithy_error_to_dafny_error,
)
from null.smithygenerated.com_amazonaws_dynamodb.shim import (
    sdk_error_to_dafny_error as com_amazonaws_dynamodb_sdk_error_to_dafny_error,
)
from null.smithygenerated.com_amazonaws_kms.shim import (
    sdk_error_to_dafny_error as com_amazonaws_kms_sdk_error_to_dafny_error,
)
from software_amazon_cryptography_materialproviders_internaldafny_types import (
    AlgorithmSuiteInfo_AlgorithmSuiteInfo as DafnyAlgorithmSuiteInfo,
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
    DecryptionMaterials_DecryptionMaterials as DafnyDecryptionMaterials,
    EncryptionMaterials_EncryptionMaterials as DafnyEncryptionMaterials,
    InitializeDecryptionMaterialsInput_InitializeDecryptionMaterialsInput as DafnyInitializeDecryptionMaterialsInput,
    InitializeEncryptionMaterialsInput_InitializeEncryptionMaterialsInput as DafnyInitializeEncryptionMaterialsInput,
    ValidDecryptionMaterialsTransitionInput_ValidDecryptionMaterialsTransitionInput as DafnyValidDecryptionMaterialsTransitionInput,
    ValidEncryptionMaterialsTransitionInput_ValidEncryptionMaterialsTransitionInput as DafnyValidEncryptionMaterialsTransitionInput,
    ValidateCommitmentPolicyOnDecryptInput_ValidateCommitmentPolicyOnDecryptInput as DafnyValidateCommitmentPolicyOnDecryptInput,
    ValidateCommitmentPolicyOnEncryptInput_ValidateCommitmentPolicyOnEncryptInput as DafnyValidateCommitmentPolicyOnEncryptInput,
)
from typing import Any

from .errors import (
    AwsCryptographicPrimitives,
    CollectionOfErrors,
    DynamoDB_20120810,
    KeyStore,
    OpaqueError,
    ServiceError,
    TrentService,
)


import Wrappers
import software_amazon_cryptography_materialproviders_internaldafny_types
import aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.client as client_impl

def smithy_error_to_dafny_error(e: ServiceError):
    '''
    Converts the provided native Smithy-modelled error
    into the corresponding Dafny error.
    '''
    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.AwsCryptographicMaterialProvidersException):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.EntryAlreadyExists):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryAlreadyExists(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.EntryDoesNotExist):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_EntryDoesNotExist(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfo):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfo(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfoOnDecrypt):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnDecrypt(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidAlgorithmSuiteInfoOnEncrypt):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidAlgorithmSuiteInfoOnEncrypt(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidDecryptionMaterials):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterials(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidDecryptionMaterialsTransition):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidEncryptionMaterials):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterials(message=e.message)

    if isinstance(e, aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.errors.InvalidEncryptionMaterialsTransition):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(message=e.message)

    if isinstance(e, AwsCryptographicPrimitives):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicPrimitives(aws_cryptography_primitives_smithy_error_to_dafny_error(e.message))

    if isinstance(e, DynamoDB_20120810):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_DynamoDB_20120810(com_amazonaws_dynamodb_sdk_error_to_dafny_error(e.message))

    if isinstance(e, TrentService):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_TrentService(com_amazonaws_kms_sdk_error_to_dafny_error(e.message))

    if isinstance(e, KeyStore):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_KeyStore(aws_cryptography_keystore_smithy_error_to_dafny_error(e.message))

    if isinstance(e, CollectionOfErrors):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(message=e.message, list=e.list)

    if isinstance(e, OpaqueError):
        return software_amazon_cryptography_materialproviders_internaldafny_types.Error_Opaque(obj=e.obj)

class MaterialProvidersShim(software_amazon_cryptography_materialproviders_internaldafny_types.IAwsCryptographicMaterialProvidersClient):
    def __init__(self, _impl: client_impl) :
        self._impl = _impl

    def CreateAwsKmsKeyring(self, input):
        smithy_client_request: CreateAwsKmsKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsDiscoveryKeyring(self, input):
        smithy_client_request: CreateAwsKmsDiscoveryKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_discovery_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMultiKeyring(self, input):
        smithy_client_request: CreateAwsKmsMultiKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsDiscoveryMultiKeyring(self, input):
        smithy_client_request: CreateAwsKmsDiscoveryMultiKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsDiscoveryMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_discovery_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkKeyring(self, input):
        smithy_client_request: CreateAwsKmsMrkKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkMultiKeyring(self, input):
        smithy_client_request: CreateAwsKmsMrkMultiKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkDiscoveryKeyring(self, input):
        smithy_client_request: CreateAwsKmsMrkDiscoveryKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_discovery_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsMrkDiscoveryMultiKeyring(self, input):
        smithy_client_request: CreateAwsKmsMrkDiscoveryMultiKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsMrkDiscoveryMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_mrk_discovery_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsHierarchicalKeyring(self, input):
        smithy_client_request: CreateAwsKmsHierarchicalKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsHierarchicalKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_hierarchical_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateMultiKeyring(self, input):
        smithy_client_request: CreateMultiKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateMultiKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_multi_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateRawAesKeyring(self, input):
        smithy_client_request: CreateRawAesKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateRawAesKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_raw_aes_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateRawRsaKeyring(self, input):
        smithy_client_request: CreateRawRsaKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateRawRsaKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_raw_rsa_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateAwsKmsRsaKeyring(self, input):
        smithy_client_request: CreateAwsKmsRsaKeyringInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateAwsKmsRsaKeyringInput(input)
        try:
            smithy_client_response = self._impl.create_aws_kms_rsa_keyring(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateKeyringOutput(smithy_client_response))

    def CreateDefaultCryptographicMaterialsManager(self, input):
        smithy_client_request: CreateDefaultCryptographicMaterialsManagerInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateDefaultCryptographicMaterialsManagerInput(input)
        try:
            smithy_client_response = self._impl.create_default_cryptographic_materials_manager(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateCryptographicMaterialsManagerOutput(smithy_client_response))

    def CreateRequiredEncryptionContextCMM(self, input):
        smithy_client_request: CreateRequiredEncryptionContextCMMInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMInput(input)
        try:
            smithy_client_response = self._impl.create_required_encryption_context_cmm(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateRequiredEncryptionContextCMMOutput(smithy_client_response))

    def CreateCryptographicMaterialsCache(self, input):
        smithy_client_request: CreateCryptographicMaterialsCacheInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheInput(input)
        try:
            smithy_client_response = self._impl.create_cryptographic_materials_cache(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateCryptographicMaterialsCacheOutput(smithy_client_response))

    def CreateDefaultClientSupplier(self, input):
        smithy_client_request: CreateDefaultClientSupplierInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_CreateDefaultClientSupplierInput(input)
        try:
            smithy_client_response = self._impl.create_default_client_supplier(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_CreateDefaultClientSupplierOutput(smithy_client_response))

    def InitializeEncryptionMaterials(self, input):
        smithy_client_request: InitializeEncryptionMaterialsInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_InitializeEncryptionMaterialsInput(input)
        try:
            smithy_client_response = self._impl.initialize_encryption_materials(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_EncryptionMaterials(smithy_client_response))

    def InitializeDecryptionMaterials(self, input):
        smithy_client_request: InitializeDecryptionMaterialsInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_InitializeDecryptionMaterialsInput(input)
        try:
            smithy_client_response = self._impl.initialize_decryption_materials(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_DecryptionMaterials(smithy_client_response))

    def ValidEncryptionMaterialsTransition(self, input):
        smithy_client_request: ValidEncryptionMaterialsTransitionInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ValidEncryptionMaterialsTransitionInput(input)
        try:
            smithy_client_response = self._impl.valid_encryption_materials_transition(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidDecryptionMaterialsTransition(self, input):
        smithy_client_request: ValidDecryptionMaterialsTransitionInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ValidDecryptionMaterialsTransitionInput(input)
        try:
            smithy_client_response = self._impl.valid_decryption_materials_transition(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def EncryptionMaterialsHasPlaintextDataKey(self, input):
        smithy_client_request: EncryptionMaterials = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_EncryptionMaterials(input)
        try:
            smithy_client_response = self._impl.encryption_materials_has_plaintext_data_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def DecryptionMaterialsWithPlaintextDataKey(self, input):
        smithy_client_request: DecryptionMaterials = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_DecryptionMaterials(input)
        try:
            smithy_client_response = self._impl.decryption_materials_with_plaintext_data_key(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def GetAlgorithmSuiteInfo(self, input):
        smithy_client_request: GetAlgorithmSuiteInfoInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_GetAlgorithmSuiteInfoInput(input)
        try:
            smithy_client_response = self._impl.get_algorithm_suite_info(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.smithy_to_dafny.SmithyToDafny_aws_cryptography_materialproviders_AlgorithmSuiteInfo(smithy_client_response))

    def ValidAlgorithmSuiteInfo(self, input):
        smithy_client_request: AlgorithmSuiteInfo = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_AlgorithmSuiteInfo(input)
        try:
            smithy_client_response = self._impl.valid_algorithm_suite_info(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidateCommitmentPolicyOnEncrypt(self, input):
        smithy_client_request: ValidateCommitmentPolicyOnEncryptInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnEncryptInput(input)
        try:
            smithy_client_response = self._impl.validate_commitment_policy_on_encrypt(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)

    def ValidateCommitmentPolicyOnDecrypt(self, input):
        smithy_client_request: ValidateCommitmentPolicyOnDecryptInput = aws_cryptography_materialproviderstestvectorkeys.smithygenerated.aws_cryptography_materialproviders.dafny_to_smithy.DafnyToSmithy_aws_cryptography_materialproviders_ValidateCommitmentPolicyOnDecryptInput(input)
        try:
            smithy_client_response = self._impl.validate_commitment_policy_on_decrypt(smithy_client_request)
        except ServiceError as e:
            return Wrappers.Result_Failure(smithy_error_to_dafny_error(e))

        return Wrappers.Result_Success(None)
