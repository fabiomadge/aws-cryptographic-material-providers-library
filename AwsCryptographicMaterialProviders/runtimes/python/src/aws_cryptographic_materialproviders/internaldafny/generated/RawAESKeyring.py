import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import BoundedInts
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UTF8
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_primitives_internaldafny_types
import ExternRandom
import Random
import AESEncryption
import ExternDigest
import Digest
import HMAC
import WrappedHMAC
import HKDF
import WrappedHKDF
import Signature
import KdfCtr
import RSAEncryption
import AwsCryptographyPrimitivesOperations
import AesKdfCtr
import Relations
import Seq_MergeSort
import Math
import Seq
import Unicode
import Functions
import Utf8EncodingForm
import Utf16EncodingForm
import UnicodeStrings
import FileIO
import GeneralInternals
import MulInternalsNonlinear
import MulInternals
import Mul
import ModInternalsNonlinear
import DivInternalsNonlinear
import ModInternals
import DivInternals
import DivMod
import Power
import Logarithm
import StandardLibraryInterop
import UUID
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import GetOpt
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_materialproviders_internaldafny_types
import AwsArnParsing
import AwsKmsMrkMatchForDecrypt
import AwsKmsUtils
import Structure
import KMSKeystoreOperations
import DDBKeystoreOperations
import CreateKeys
import CreateKeyStoreTable
import GetKeys
import AwsCryptographyKeyStoreOperations
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import Com_Amazonaws
import Com
import software_amazon_cryptography_keystore_internaldafny
import AlgorithmSuites
import Materials
import Keyring
import MultiKeyring
import AwsKmsMrkAreUnique
import Constants
import software_amazon_cryptography_primitives_internaldafny
import Aws_Cryptography
import Aws
import MaterialWrapping
import CanonicalEncryptionContext
import IntermediateKeyWrapping
import EdkWrapping
import AwsKmsKeyring
import StrictMultiKeyring
import AwsKmsDiscoveryKeyring
import DiscoveryMultiKeyring
import AwsKmsMrkDiscoveryKeyring
import MrkAwareDiscoveryMultiKeyring
import AwsKmsMrkKeyring
import MrkAwareStrictMultiKeyring
import LocalCMC
import software_amazon_cryptography_internaldafny_SynchronizedLocalCMC
import StormTracker
import software_amazon_cryptography_internaldafny_StormTrackingCMC
import AwsKmsHierarchicalKeyring
import AwsKmsRsaKeyring

# Module: RawAESKeyring

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeserializeEDKCiphertext(ciphertext, tagLen):
        d_1060_encryptedKeyLength_ = (len(ciphertext)) - (tagLen)
        return software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput_AESEncryptOutput(_dafny.Seq((ciphertext)[:d_1060_encryptedKeyLength_:]), _dafny.Seq((ciphertext)[d_1060_encryptedKeyLength_::]))

    @staticmethod
    def SerializeEDKCiphertext(encOutput):
        return ((encOutput).cipherText) + ((encOutput).authTag)

    @_dafny.classproperty
    def AUTH__TAG__LEN__LEN(instance):
        return 4
    @_dafny.classproperty
    def IV__LEN__LEN(instance):
        return 4

class RawAESKeyring(Keyring.VerifiableInterface, software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring):
    def  __init__(self):
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._keyNamespace: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        self._keyName: _dafny.Seq = UTF8.ValidUTF8Bytes.default()
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.RawAESKeyring"
    def OnEncrypt(self, input):
        out193_: Wrappers.Result
        out193_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnEncrypt(self, input)
        return out193_

    def OnDecrypt(self, input):
        out194_: Wrappers.Result
        out194_ = software_amazon_cryptography_materialproviders_internaldafny_types.IKeyring.OnDecrypt(self, input)
        return out194_

    def ctor__(self, namespace, name, key, wrappingAlgorithm, cryptoPrimitives):
        (self)._keyNamespace = namespace
        (self)._keyName = name
        (self)._wrappingKey = key
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def OnEncrypt_k(self, input):
        output: Wrappers.Result = None
        d_1061_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
        d_1061_materials_ = (input).materials
        d_1062_suite_: software_amazon_cryptography_materialproviders_internaldafny_types.AlgorithmSuiteInfo
        d_1062_suite_ = (d_1061_materials_).algorithmSuite
        d_1063_wrap_: AesWrapKeyMaterial
        nw45_ = AesWrapKeyMaterial()
        nw45_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, (self).cryptoPrimitives)
        d_1063_wrap_ = nw45_
        d_1064_generateAndWrap_: AesGenerateAndWrapKeyMaterial
        nw46_ = AesGenerateAndWrapKeyMaterial()
        nw46_.ctor__(d_1063_wrap_)
        d_1064_generateAndWrap_ = nw46_
        d_1065_wrapOutput_: EdkWrapping.WrapEdkMaterialOutput
        d_1066_valueOrError0_: Wrappers.Result = Wrappers.Result.default(EdkWrapping.WrapEdkMaterialOutput.default(AesWrapInfo.default()))()
        out195_: Wrappers.Result
        out195_ = EdkWrapping.default__.WrapEdkMaterial(d_1061_materials_, d_1063_wrap_, d_1064_generateAndWrap_)
        d_1066_valueOrError0_ = out195_
        if (d_1066_valueOrError0_).IsFailure():
            output = (d_1066_valueOrError0_).PropagateFailure()
            return output
        d_1065_wrapOutput_ = (d_1066_valueOrError0_).Extract()
        d_1067_symmetricSigningKeyList_: Wrappers.Option
        d_1067_symmetricSigningKeyList_ = (Wrappers.Option_Some(_dafny.Seq([((d_1065_wrapOutput_).symmetricSigningKey).value])) if ((d_1065_wrapOutput_).symmetricSigningKey).is_Some else Wrappers.Option_None())
        d_1068_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
        d_1068_edk_ = software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey_EncryptedDataKey((self).keyNamespace, (self).SerializeProviderInfo(((d_1065_wrapOutput_).wrapInfo).iv), (d_1065_wrapOutput_).wrappedMaterial)
        if (d_1065_wrapOutput_).is_GenerateAndWrapEdkMaterialOutput:
            d_1069_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1070_valueOrError1_: Wrappers.Result = None
            d_1070_valueOrError1_ = Materials.default__.EncryptionMaterialAddDataKey(d_1061_materials_, (d_1065_wrapOutput_).plaintextDataKey, _dafny.Seq([d_1068_edk_]), d_1067_symmetricSigningKeyList_)
            if (d_1070_valueOrError1_).IsFailure():
                output = (d_1070_valueOrError1_).PropagateFailure()
                return output
            d_1069_result_ = (d_1070_valueOrError1_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1069_result_))
            return output
        elif (d_1065_wrapOutput_).is_WrapOnlyEdkMaterialOutput:
            d_1071_result_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials
            d_1072_valueOrError2_: Wrappers.Result = None
            d_1072_valueOrError2_ = Materials.default__.EncryptionMaterialAddEncryptedDataKeys(d_1061_materials_, _dafny.Seq([d_1068_edk_]), d_1067_symmetricSigningKeyList_)
            if (d_1072_valueOrError2_).IsFailure():
                output = (d_1072_valueOrError2_).PropagateFailure()
                return output
            d_1071_result_ = (d_1072_valueOrError2_).Extract()
            output = Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.OnEncryptOutput_OnEncryptOutput(d_1071_result_))
            return output
        return output

    def OnDecrypt_k(self, input):
        output: Wrappers.Result = None
        d_1073_materials_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
        d_1073_materials_ = (input).materials
        d_1074_valueOrError0_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1074_valueOrError0_ = Wrappers.default__.Need(Materials.default__.DecryptionMaterialsWithoutPlaintextDataKey(d_1073_materials_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Keyring received decryption materials that already contain a plaintext data key.")))
        if (d_1074_valueOrError0_).IsFailure():
            output = (d_1074_valueOrError0_).PropagateFailure()
            return output
        d_1075_aad_: _dafny.Seq
        d_1076_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1076_valueOrError1_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD(((input).materials).encryptionContext)
        if (d_1076_valueOrError1_).IsFailure():
            output = (d_1076_valueOrError1_).PropagateFailure()
            return output
        d_1075_aad_ = (d_1076_valueOrError1_).Extract()
        d_1077_valueOrError2_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1077_valueOrError2_ = Wrappers.default__.Need((len((self).wrappingKey)) == (((self).wrappingAlgorithm).keyLength), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("The wrapping key does not match the wrapping algorithm")))
        if (d_1077_valueOrError2_).IsFailure():
            output = (d_1077_valueOrError2_).PropagateFailure()
            return output
        d_1078_errors_: _dafny.Seq
        d_1078_errors_ = _dafny.Seq([])
        hi8_ = len((input).encryptedDataKeys)
        for d_1079_i_ in range(0, hi8_):
            if (self).ShouldDecryptEDK(((input).encryptedDataKeys)[d_1079_i_]):
                d_1080_edk_: software_amazon_cryptography_materialproviders_internaldafny_types.EncryptedDataKey
                d_1080_edk_ = ((input).encryptedDataKeys)[d_1079_i_]
                d_1081_iv_: _dafny.Seq
                d_1081_iv_ = (self).GetIvFromProvInfo((d_1080_edk_).keyProviderInfo)
                d_1082_unwrap_: AesUnwrapKeyMaterial
                nw47_ = AesUnwrapKeyMaterial()
                nw47_.ctor__((self).wrappingKey, (self).wrappingAlgorithm, d_1081_iv_, (self).cryptoPrimitives)
                d_1082_unwrap_ = nw47_
                d_1083_unwrapOutput_: Wrappers.Result
                out196_: Wrappers.Result
                out196_ = EdkWrapping.default__.UnwrapEdkMaterial((d_1080_edk_).ciphertext, d_1073_materials_, d_1082_unwrap_)
                d_1083_unwrapOutput_ = out196_
                if (d_1083_unwrapOutput_).is_Success:
                    d_1084_result_: software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials
                    d_1085_valueOrError3_: Wrappers.Result = None
                    d_1085_valueOrError3_ = Materials.default__.DecryptionMaterialsAddDataKey(d_1073_materials_, ((d_1083_unwrapOutput_).value).plaintextDataKey, ((d_1083_unwrapOutput_).value).symmetricSigningKey)
                    if (d_1085_valueOrError3_).IsFailure():
                        output = (d_1085_valueOrError3_).PropagateFailure()
                        return output
                    d_1084_result_ = (d_1085_valueOrError3_).Extract()
                    d_1086_value_: software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput
                    d_1086_value_ = software_amazon_cryptography_materialproviders_internaldafny_types.OnDecryptOutput_OnDecryptOutput(d_1084_result_)
                    output = Wrappers.Result_Success(d_1086_value_)
                    return output
                elif True:
                    d_1078_errors_ = (d_1078_errors_) + (_dafny.Seq([(d_1083_unwrapOutput_).error]))
            elif True:
                d_1078_errors_ = (d_1078_errors_) + (_dafny.Seq([software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(((_dafny.Seq("EncrypedDataKey ")) + (StandardLibrary_String.default__.Base10Int2String(d_1079_i_))) + (_dafny.Seq(" did not match AESKeyring. ")))]))
        output = Wrappers.Result_Failure(software_amazon_cryptography_materialproviders_internaldafny_types.Error_CollectionOfErrors(d_1078_errors_, _dafny.Seq("Raw AES Keyring was unable to decrypt any encrypted data key. The list of encountered Exceptions is avaible via `list`.")))
        return output
        return output

    def SerializeProviderInfo(self, iv):
        return ((((self).keyName) + (StandardLibrary_UInt.default__.UInt32ToSeq((((self).wrappingAlgorithm).tagLength) * (8)))) + (StandardLibrary_UInt.default__.UInt32ToSeq(((self).wrappingAlgorithm).ivLength))) + (iv)

    def ShouldDecryptEDK(self, edk):
        return (((edk).keyProviderId) == ((self).keyNamespace)) and ((self).ValidProviderInfo((edk).keyProviderInfo))

    def ValidProviderInfo(self, info):
        return ((((((len(info)) == ((((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN)) + (((self).wrappingAlgorithm).ivLength))) and ((_dafny.Seq((info)[0:len((self).keyName):])) == ((self).keyName))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):]))) == (128))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[len((self).keyName):(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):]))) == ((((self).wrappingAlgorithm).tagLength) * (8)))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN):]))) == (((self).wrappingAlgorithm).ivLength))) and ((StandardLibrary_UInt.default__.SeqToUInt32(_dafny.Seq((info)[(len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN):((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN):]))) == (12))

    def GetIvFromProvInfo(self, info):
        return _dafny.Seq((info)[((len((self).keyName)) + (default__.AUTH__TAG__LEN__LEN)) + (default__.IV__LEN__LEN)::])

    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def keyNamespace(self):
        return self._keyNamespace
    @property
    def keyName(self):
        return self._keyName

class AesUnwrapInfo:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [AesUnwrapInfo_AesUnwrapInfo()]
    @classmethod
    def default(cls, ):
        return lambda: AesUnwrapInfo_AesUnwrapInfo()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AesUnwrapInfo(self) -> bool:
        return isinstance(self, AesUnwrapInfo_AesUnwrapInfo)

class AesUnwrapInfo_AesUnwrapInfo(AesUnwrapInfo, NamedTuple('AesUnwrapInfo', [])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesUnwrapInfo.AesUnwrapInfo'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesUnwrapInfo_AesUnwrapInfo)
    def __hash__(self) -> int:
        return super().__hash__()


class AesWrapInfo:
    @classmethod
    def default(cls, ):
        return lambda: AesWrapInfo_AesWrapInfo(_dafny.Seq({}))
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_AesWrapInfo(self) -> bool:
        return isinstance(self, AesWrapInfo_AesWrapInfo)

class AesWrapInfo_AesWrapInfo(AesWrapInfo, NamedTuple('AesWrapInfo', [('iv', Any)])):
    def __dafnystr__(self) -> str:
        return f'RawAESKeyring.AesWrapInfo.AesWrapInfo({_dafny.string_of(self.iv)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, AesWrapInfo_AesWrapInfo) and self.iv == __o.iv
    def __hash__(self) -> int:
        return super().__hash__()


class AesGenerateAndWrapKeyMaterial(MaterialWrapping.GenerateAndWrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrap: AesWrapKeyMaterial = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesGenerateAndWrapKeyMaterial"
    def ctor__(self, wrap):
        (self)._wrap = wrap

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.GenerateAndWrapOutput.default(AesWrapInfo.default()))()
        d_1087_generateBytesResult_: Wrappers.Result
        out197_: Wrappers.Result
        out197_ = (((self).wrap).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)))
        d_1087_generateBytesResult_ = out197_
        d_1088_plaintextMaterial_: _dafny.Seq
        d_1089_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda84_(d_1090_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1090_e_)

        d_1089_valueOrError0_ = (d_1087_generateBytesResult_).MapFailure(lambda84_)
        if (d_1089_valueOrError0_).IsFailure():
            res = (d_1089_valueOrError0_).PropagateFailure()
            return res
        d_1088_plaintextMaterial_ = (d_1089_valueOrError0_).Extract()
        d_1091_wrapOutput_: MaterialWrapping.WrapOutput
        d_1092_valueOrError1_: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        out198_: Wrappers.Result
        out198_ = ((self).wrap).Invoke(MaterialWrapping.WrapInput_WrapInput(d_1088_plaintextMaterial_, (input).algorithmSuite, (input).encryptionContext))
        d_1092_valueOrError1_ = out198_
        if (d_1092_valueOrError1_).IsFailure():
            res = (d_1092_valueOrError1_).PropagateFailure()
            return res
        d_1091_wrapOutput_ = (d_1092_valueOrError1_).Extract()
        res = Wrappers.Result_Success(MaterialWrapping.GenerateAndWrapOutput_GenerateAndWrapOutput(d_1088_plaintextMaterial_, (d_1091_wrapOutput_).wrappedMaterial, (d_1091_wrapOutput_).wrapInfo))
        return res

    @property
    def wrap(self):
        return self._wrap

class AesWrapKeyMaterial(MaterialWrapping.WrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesWrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.WrapOutput.default(AesWrapInfo.default()))()
        d_1093_aad_: _dafny.Seq
        d_1094_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1094_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1094_valueOrError0_).IsFailure():
            res = (d_1094_valueOrError0_).PropagateFailure()
            return res
        d_1093_aad_ = (d_1094_valueOrError0_).Extract()
        d_1095_randomIvResult_: Wrappers.Result
        out199_: Wrappers.Result
        out199_ = ((self).cryptoPrimitives).GenerateRandomBytes(software_amazon_cryptography_primitives_internaldafny_types.GenerateRandomBytesInput_GenerateRandomBytesInput(((self).wrappingAlgorithm).ivLength))
        d_1095_randomIvResult_ = out199_
        d_1096_iv_: _dafny.Seq
        d_1097_valueOrError1_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda85_(d_1098_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1098_e_)

        d_1097_valueOrError1_ = (d_1095_randomIvResult_).MapFailure(lambda85_)
        if (d_1097_valueOrError1_).IsFailure():
            res = (d_1097_valueOrError1_).PropagateFailure()
            return res
        d_1096_iv_ = (d_1097_valueOrError1_).Extract()
        d_1099_aesEncryptResult_: Wrappers.Result
        out200_: Wrappers.Result
        out200_ = ((self).cryptoPrimitives).AESEncrypt(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptInput_AESEncryptInput((self).wrappingAlgorithm, d_1096_iv_, (self).wrappingKey, (input).plaintextMaterial, d_1093_aad_))
        d_1099_aesEncryptResult_ = out200_
        d_1100_wrappedMaterialResult_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1101_valueOrError2_: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        def lambda86_(d_1102_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1102_e_)

        d_1101_valueOrError2_ = (d_1099_aesEncryptResult_).MapFailure(lambda86_)
        if (d_1101_valueOrError2_).IsFailure():
            res = (d_1101_valueOrError2_).PropagateFailure()
            return res
        d_1100_wrappedMaterialResult_ = (d_1101_valueOrError2_).Extract()
        d_1103_wrappedMaterial_: _dafny.Seq
        d_1103_wrappedMaterial_ = default__.SerializeEDKCiphertext(d_1100_wrappedMaterialResult_)
        res = Wrappers.Result_Success(MaterialWrapping.WrapOutput_WrapOutput(d_1103_wrappedMaterial_, AesWrapInfo_AesWrapInfo(d_1096_iv_)))
        return res
        return res

    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives

class AesUnwrapKeyMaterial(MaterialWrapping.UnwrapMaterial, Actions.ActionWithResult, Actions.Action):
    def  __init__(self):
        self._wrappingKey: _dafny.Seq = _dafny.Seq({})
        self._iv: _dafny.Seq = _dafny.Seq({})
        self._wrappingAlgorithm: software_amazon_cryptography_primitives_internaldafny_types.AES__GCM = None
        self._cryptoPrimitives: software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient = None
        pass

    def __dafnystr__(self) -> str:
        return "RawAESKeyring.AesUnwrapKeyMaterial"
    def ctor__(self, wrappingKey, wrappingAlgorithm, iv, cryptoPrimitives):
        (self)._wrappingKey = wrappingKey
        (self)._iv = iv
        (self)._wrappingAlgorithm = wrappingAlgorithm
        (self)._cryptoPrimitives = cryptoPrimitives

    def Invoke(self, input):
        res: Wrappers.Result = Wrappers.Result.default(MaterialWrapping.UnwrapOutput.default(AesUnwrapInfo.default()))()
        d_1104_aad_: _dafny.Seq
        d_1105_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_1105_valueOrError0_ = CanonicalEncryptionContext.default__.EncryptionContextToAAD((input).encryptionContext)
        if (d_1105_valueOrError0_).IsFailure():
            res = (d_1105_valueOrError0_).PropagateFailure()
            return res
        d_1104_aad_ = (d_1105_valueOrError0_).Extract()
        d_1106_valueOrError1_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1106_valueOrError1_ = Wrappers.default__.Need((((self).wrappingAlgorithm).tagLength) <= (len((input).wrappedMaterial)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Insufficient data to decrypt.")))
        if (d_1106_valueOrError1_).IsFailure():
            res = (d_1106_valueOrError1_).PropagateFailure()
            return res
        d_1107_encryptionOutput_: software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput
        d_1107_encryptionOutput_ = default__.DeserializeEDKCiphertext((input).wrappedMaterial, ((self).wrappingAlgorithm).tagLength)
        d_1108_maybePtKey_: Wrappers.Result
        out201_: Wrappers.Result
        out201_ = ((self).cryptoPrimitives).AESDecrypt(software_amazon_cryptography_primitives_internaldafny_types.AESDecryptInput_AESDecryptInput((self).wrappingAlgorithm, (self).wrappingKey, (d_1107_encryptionOutput_).cipherText, (d_1107_encryptionOutput_).authTag, (self).iv, d_1104_aad_))
        d_1108_maybePtKey_ = out201_
        d_1109_ptKey_: _dafny.Seq
        d_1110_valueOrError2_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        def lambda87_(d_1111_e_):
            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographyPrimitives(d_1111_e_)

        d_1110_valueOrError2_ = (d_1108_maybePtKey_).MapFailure(lambda87_)
        if (d_1110_valueOrError2_).IsFailure():
            res = (d_1110_valueOrError2_).PropagateFailure()
            return res
        d_1109_ptKey_ = (d_1110_valueOrError2_).Extract()
        d_1112_valueOrError3_: Wrappers.Outcome = Wrappers.Outcome.default()()
        d_1112_valueOrError3_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength((input).algorithmSuite)) == (len(d_1109_ptKey_)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Plaintext Data Key is not the expected length")))
        if (d_1112_valueOrError3_).IsFailure():
            res = (d_1112_valueOrError3_).PropagateFailure()
            return res
        res = Wrappers.Result_Success(MaterialWrapping.UnwrapOutput_UnwrapOutput(d_1109_ptKey_, AesUnwrapInfo_AesUnwrapInfo()))
        return res
        return res

    @property
    def wrappingKey(self):
        return self._wrappingKey
    @property
    def iv(self):
        return self._iv
    @property
    def wrappingAlgorithm(self):
        return self._wrappingAlgorithm
    @property
    def cryptoPrimitives(self):
        return self._cryptoPrimitives
