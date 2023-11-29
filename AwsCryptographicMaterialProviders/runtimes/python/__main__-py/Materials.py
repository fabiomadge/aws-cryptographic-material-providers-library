import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_mMergeSort
import Math
import Seq
import BoundedInts
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
import StandardLibrary_mUInt
import String
import StandardLibrary
import UUID
import UTF8
import Time
import Streams
import Sorting
import SortedSets
import HexStrings
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import DafnyLibraries
import software_amazon_cryptography_services_dynamodb_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny_types
import software_amazon_cryptography_keystore_internaldafny_types
import software_amazon_cryptography_services_kms_internaldafny
import software_amazon_cryptography_services_dynamodb_internaldafny
import software_amazon_cryptography_primitives_internaldafny_types
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
import software_amazon_cryptography_keystore_internaldafny
import Fixtures
import TestCreateKeyStore
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
import TestConfig
import TestGetKeys
import CleanupItems
import TestCreateKeys
import TestVersionKey
import AlgorithmSuites

assert "Materials" == __name__
Materials = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def InitializeEncryptionMaterials(input):
        pat_let_tv0_ = input
        pat_let_tv1_ = input
        pat_let_tv2_ = input
        d_603_valueOrError0_ = Wrappers.default__.Need(((Materials.default__).EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context ")))
        if (d_603_valueOrError0_).IsFailure():
            return (d_603_valueOrError0_).PropagateFailure()
        elif True:
            def lambda32_(forall_var_9_):
                d_605_key_: _dafny.Seq = forall_var_9_
                return not ((d_605_key_) in ((input).requiredEncryptionContextKeys)) or ((d_605_key_) in ((input).encryptionContext))

            d_604_valueOrError1_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda32_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Required encryption context keys do not exist in provided encryption context.")))
            if (d_604_valueOrError1_).IsFailure():
                return (d_604_valueOrError1_).PropagateFailure()
            elif True:
                d_606_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
                d_607_valueOrError2_ = Wrappers.default__.Need((((d_606_suite_).signature).is_ECDSA) == ((((input).signingKey).is_Some) and (((input).verificationKey).is_Some)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Missing signature key for signed suite.")))
                if (d_607_valueOrError2_).IsFailure():
                    return (d_607_valueOrError2_).PropagateFailure()
                elif True:
                    d_608_valueOrError3_ = Wrappers.default__.Need((((d_606_suite_).signature).is_None) == ((((input).signingKey).is_None) and (((input).verificationKey).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Signature key not allowed for non-signed suites.")))
                    if (d_608_valueOrError3_).IsFailure():
                        return (d_608_valueOrError3_).PropagateFailure()
                    elif True:
                        def lambda33_(source21_):
                            if source21_.is_ECDSA:
                                d_610___mcc_h0_ = source21_.ECDSA
                                def iife15_(_pat_let2_0):
                                    def iife16_(d_611_curve_):
                                        def lambda34_(d_612_e_):
                                            return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_612_e_)

                                        def iife17_(_pat_let3_0):
                                            def iife18_(d_613_valueOrError5_):
                                                def iife19_(_pat_let4_0):
                                                    def iife20_(d_614_enc__vk_):
                                                        return Wrappers.Result_Success(((pat_let_tv1_).encryptionContext).set((Materials.default__).EC__PUBLIC__KEY__FIELD, d_614_enc__vk_))
                                                    return iife20_(_pat_let4_0)
                                                return ((d_613_valueOrError5_).PropagateFailure() if (d_613_valueOrError5_).IsFailure() else iife19_((d_613_valueOrError5_).Extract()))
                                            return iife18_(_pat_let3_0)
                                        return iife17_((UTF8.default__.Encode(Base64.default__.Encode(((pat_let_tv0_).verificationKey).value))).MapFailure(lambda34_))
                                    return iife16_(_pat_let2_0)
                                return iife15_(d_610___mcc_h0_)
                            elif True:
                                d_615___mcc_h2_ = source21_.None_
                                def iife21_(_pat_let5_0):
                                    def iife22_(d_616_None_):
                                        return Wrappers.Result_Success((pat_let_tv2_).encryptionContext)
                                    return iife22_(_pat_let5_0)
                                return iife21_((d_606_suite_).signature)

                        d_609_valueOrError4_ = lambda33_((d_606_suite_).signature)
                        if (d_609_valueOrError4_).IsFailure():
                            return (d_609_valueOrError4_).PropagateFailure()
                        elif True:
                            d_617_encryptionContext_ = (d_609_valueOrError4_).Extract()
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials(d_606_suite_, d_617_encryptionContext_, _dafny.Seq([]), (input).requiredEncryptionContextKeys, Wrappers.Option_None(), (input).signingKey, (Wrappers.Option_None() if ((d_606_suite_).symmetricSignature).is_None else Wrappers.Option_Some(_dafny.Seq([])))))

    @staticmethod
    def InitializeDecryptionMaterials(input):
        def lambda35_(forall_var_10_):
            d_619_key_: _dafny.Seq = forall_var_10_
            return not ((d_619_key_) in ((input).requiredEncryptionContextKeys)) or ((d_619_key_) in ((input).encryptionContext))

        d_618_valueOrError0_ = Wrappers.default__.Need(_dafny.quantifier(((input).requiredEncryptionContextKeys).UniqueElements, True, lambda35_), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Reporoduced encryption context key did not exist in provided encryption context.")))
        if (d_618_valueOrError0_).IsFailure():
            return (d_618_valueOrError0_).PropagateFailure()
        elif True:
            d_620_suite_ = AlgorithmSuites.default__.GetSuite((input).algorithmSuiteId)
            d_621_valueOrError1_ = Wrappers.default__.Need((((d_620_suite_).signature).is_ECDSA) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) in ((input).encryptionContext)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Encryption Context missing verification key.")))
            if (d_621_valueOrError1_).IsFailure():
                return (d_621_valueOrError1_).PropagateFailure()
            elif True:
                d_622_valueOrError2_ = Wrappers.default__.Need((((d_620_suite_).signature).is_None) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) not in ((input).encryptionContext)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(_dafny.Seq("Verification key can not exist in non-signed Algorithm Suites.")))
                if (d_622_valueOrError2_).IsFailure():
                    return (d_622_valueOrError2_).PropagateFailure()
                elif True:
                    d_623_valueOrError3_ = Materials.default__.DecodeVerificationKey((input).encryptionContext)
                    if (d_623_valueOrError3_).IsFailure():
                        return (d_623_valueOrError3_).PropagateFailure()
                    elif True:
                        d_624_verificationKey_ = (d_623_valueOrError3_).Extract()
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials(d_620_suite_, (input).encryptionContext, (input).requiredEncryptionContextKeys, Wrappers.Option_None(), d_624_verificationKey_, Wrappers.Option_None()))

    @staticmethod
    def DecodeVerificationKey(encryptionContext):
        if ((Materials.default__).EC__PUBLIC__KEY__FIELD) in (encryptionContext):
            d_625_utf8Key_ = (encryptionContext)[(Materials.default__).EC__PUBLIC__KEY__FIELD]
            def lambda36_(d_627_e_):
                return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_627_e_)

            d_626_valueOrError0_ = (UTF8.default__.Decode(d_625_utf8Key_)).MapFailure(lambda36_)
            if (d_626_valueOrError0_).IsFailure():
                return (d_626_valueOrError0_).PropagateFailure()
            elif True:
                d_628_base64Key_ = (d_626_valueOrError0_).Extract()
                def lambda37_(d_630_e_):
                    return software_amazon_cryptography_materialproviders_internaldafny_types.Error_AwsCryptographicMaterialProvidersException(d_630_e_)

                d_629_valueOrError1_ = (Base64.default__.Decode(d_628_base64Key_)).MapFailure(lambda37_)
                if (d_629_valueOrError1_).IsFailure():
                    return (d_629_valueOrError1_).PropagateFailure()
                elif True:
                    d_631_key_ = (d_629_valueOrError1_).Extract()
                    return Wrappers.Result_Success(Wrappers.Option_Some(d_631_key_))
        elif True:
            return Wrappers.Result_Success(Wrappers.Option_None())

    @staticmethod
    def ValidEncryptionMaterialsTransition(oldMat, newMat):
        return ((((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).signingKey) == ((oldMat).signingKey))) and (((((oldMat).plaintextDataKey).is_None) and (((newMat).plaintextDataKey).is_Some)) or (((oldMat).plaintextDataKey) == ((newMat).plaintextDataKey)))) and (((newMat).plaintextDataKey).is_Some)) and ((len((oldMat).encryptedDataKeys)) <= (len((newMat).encryptedDataKeys)))) and ((_dafny.MultiSet((oldMat).encryptedDataKeys)).issubset(_dafny.MultiSet((newMat).encryptedDataKeys)))) and (not (not((((oldMat).algorithmSuite).symmetricSignature).is_None)) or (((((newMat).symmetricSigningKeys).is_Some) and (((oldMat).symmetricSigningKeys).is_Some)) and ((_dafny.MultiSet(((oldMat).symmetricSigningKeys).value)).issubset(_dafny.MultiSet(((newMat).symmetricSigningKeys).value)))))) and (Materials.default__.ValidEncryptionMaterials(oldMat))) and (Materials.default__.ValidEncryptionMaterials(newMat))

    @staticmethod
    def ValidEncryptionMaterials(encryptionMaterials):
        pat_let_tv3_ = encryptionMaterials
        pat_let_tv4_ = encryptionMaterials
        pat_let_tv5_ = encryptionMaterials
        pat_let_tv6_ = encryptionMaterials
        pat_let_tv7_ = encryptionMaterials
        pat_let_tv8_ = encryptionMaterials
        pat_let_tv9_ = encryptionMaterials
        pat_let_tv10_ = encryptionMaterials
        pat_let_tv11_ = encryptionMaterials
        pat_let_tv12_ = encryptionMaterials
        pat_let_tv13_ = encryptionMaterials
        pat_let_tv14_ = encryptionMaterials
        pat_let_tv15_ = encryptionMaterials
        pat_let_tv16_ = encryptionMaterials
        pat_let_tv17_ = encryptionMaterials
        pat_let_tv18_ = encryptionMaterials
        def iife23_(_pat_let6_0):
            def iife24_(d_632_suite_):
                def lambda38_(forall_var_11_):
                    d_633_key_: _dafny.Seq = forall_var_11_
                    return not ((d_633_key_) in ((pat_let_tv17_).requiredEncryptionContextKeys)) or ((d_633_key_) in ((pat_let_tv18_).encryptionContext))

                return ((((((((((((d_632_suite_).signature).is_None) == (((pat_let_tv3_).signingKey).is_None)) and (not (((pat_let_tv4_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_632_suite_)) == (len(((pat_let_tv5_).plaintextDataKey).value))))) and (not (((pat_let_tv6_).plaintextDataKey).is_None) or ((len((pat_let_tv7_).encryptedDataKeys)) == (0)))) and ((not(((d_632_suite_).signature).is_None)) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) in ((pat_let_tv8_).encryptionContext)))) and ((((d_632_suite_).signature).is_ECDSA) == (((pat_let_tv9_).signingKey).is_Some))) and ((not(((d_632_suite_).signature).is_None)) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) in ((pat_let_tv10_).encryptionContext)))) and (not ((((d_632_suite_).symmetricSignature).is_HMAC) and (((pat_let_tv11_).symmetricSigningKeys).is_Some)) or ((len(((pat_let_tv12_).symmetricSigningKeys).value)) == (len((pat_let_tv13_).encryptedDataKeys))))) and (not (((d_632_suite_).symmetricSignature).is_HMAC) or (((pat_let_tv14_).symmetricSigningKeys).is_Some))) and (not (((d_632_suite_).symmetricSignature).is_None) or (((pat_let_tv15_).symmetricSigningKeys).is_None))) and (_dafny.quantifier(((pat_let_tv16_).requiredEncryptionContextKeys).UniqueElements, True, lambda38_))
            return iife24_(_pat_let6_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((encryptionMaterials).algorithmSuite)) and (iife23_((encryptionMaterials).algorithmSuite))

    @staticmethod
    def EncryptionMaterialsHasPlaintextDataKey(encryptionMaterials):
        return ((((encryptionMaterials).plaintextDataKey).is_Some) and ((len((encryptionMaterials).encryptedDataKeys)) > (0))) and (Materials.default__.ValidEncryptionMaterials(encryptionMaterials))

    @staticmethod
    def EncryptionMaterialAddEncryptedDataKeys(encryptionMaterials, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_634_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_634_valueOrError0_).IsFailure():
            return (d_634_valueOrError0_).PropagateFailure()
        elif True:
            d_635_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_Some, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a plaintext data key is not allowed.")))
            if (d_635_valueOrError1_).IsFailure():
                return (d_635_valueOrError1_).PropagateFailure()
            elif True:
                d_636_valueOrError2_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_None) or ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                if (d_636_valueOrError2_).IsFailure():
                    return (d_636_valueOrError2_).PropagateFailure()
                elif True:
                    d_637_valueOrError3_ = Wrappers.default__.Need(not ((symmetricSigningKeysToAdd).is_Some) or (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                    if (d_637_valueOrError3_).IsFailure():
                        return (d_637_valueOrError3_).PropagateFailure()
                    elif True:
                        d_638_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                        return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, (encryptionMaterials).plaintextDataKey, (encryptionMaterials).signingKey, d_638_symmetricSigningKeys_))

    @staticmethod
    def EncryptionMaterialAddDataKey(encryptionMaterials, plaintextDataKey, encryptedDataKeysToAdd, symmetricSigningKeysToAdd):
        d_639_suite_ = (encryptionMaterials).algorithmSuite
        d_640_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidEncryptionMaterials(encryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid encryption material.")))
        if (d_640_valueOrError0_).IsFailure():
            return (d_640_valueOrError0_).PropagateFailure()
        elif True:
            d_641_valueOrError1_ = Wrappers.default__.Need(((encryptionMaterials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_641_valueOrError1_).IsFailure():
                return (d_641_valueOrError1_).PropagateFailure()
            elif True:
                d_642_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_639_suite_)) == (len(plaintextDataKey)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_642_valueOrError2_).IsFailure():
                    return (d_642_valueOrError2_).PropagateFailure()
                elif True:
                    d_643_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_None) == ((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys without a symmetric signing key when using symmetric signing is not allowed.")))
                    if (d_643_valueOrError3_).IsFailure():
                        return (d_643_valueOrError3_).PropagateFailure()
                    elif True:
                        d_644_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKeysToAdd).is_Some) == (not((((encryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidEncryptionMaterialsTransition(_dafny.Seq("Adding encrypted data keys with a symmetric signing key when not using symmetric signing is not allowed.")))
                        if (d_644_valueOrError4_).IsFailure():
                            return (d_644_valueOrError4_).PropagateFailure()
                        elif True:
                            d_645_symmetricSigningKeys_ = ((encryptionMaterials).symmetricSigningKeys if (symmetricSigningKeysToAdd).is_None else Wrappers.Option_Some((((encryptionMaterials).symmetricSigningKeys).value) + ((symmetricSigningKeysToAdd).value)))
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.EncryptionMaterials_EncryptionMaterials((encryptionMaterials).algorithmSuite, (encryptionMaterials).encryptionContext, ((encryptionMaterials).encryptedDataKeys) + (encryptedDataKeysToAdd), (encryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (encryptionMaterials).signingKey, d_645_symmetricSigningKeys_))

    @staticmethod
    def DecryptionMaterialsTransitionIsValid(oldMat, newMat):
        return ((((((((((newMat).algorithmSuite) == ((oldMat).algorithmSuite)) and (((newMat).encryptionContext) == ((oldMat).encryptionContext))) and (((newMat).requiredEncryptionContextKeys) == ((oldMat).requiredEncryptionContextKeys))) and (((newMat).verificationKey) == ((oldMat).verificationKey))) and (((oldMat).plaintextDataKey).is_None)) and (((newMat).plaintextDataKey).is_Some)) and (((oldMat).symmetricSigningKey).is_None)) and (Materials.default__.ValidDecryptionMaterials(oldMat))) and (Materials.default__.ValidDecryptionMaterials(newMat))

    @staticmethod
    def ValidDecryptionMaterials(decryptionMaterials):
        pat_let_tv19_ = decryptionMaterials
        pat_let_tv20_ = decryptionMaterials
        pat_let_tv21_ = decryptionMaterials
        pat_let_tv22_ = decryptionMaterials
        pat_let_tv23_ = decryptionMaterials
        pat_let_tv24_ = decryptionMaterials
        pat_let_tv25_ = decryptionMaterials
        pat_let_tv26_ = decryptionMaterials
        pat_let_tv27_ = decryptionMaterials
        pat_let_tv28_ = decryptionMaterials
        pat_let_tv29_ = decryptionMaterials
        def iife25_(_pat_let7_0):
            def iife26_(d_646_suite_):
                def lambda39_(forall_var_12_):
                    d_647_k_: _dafny.Seq = forall_var_12_
                    return not ((d_647_k_) in ((pat_let_tv28_).requiredEncryptionContextKeys)) or ((d_647_k_) in ((pat_let_tv29_).encryptionContext))

                return ((((((not (((pat_let_tv19_).plaintextDataKey).is_Some) or ((AlgorithmSuites.default__.GetEncryptKeyLength(d_646_suite_)) == (len(((pat_let_tv20_).plaintextDataKey).value)))) and ((not(((d_646_suite_).signature).is_None)) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) in ((pat_let_tv21_).encryptionContext)))) and ((((d_646_suite_).signature).is_ECDSA) == (((pat_let_tv22_).verificationKey).is_Some))) and ((not(((d_646_suite_).signature).is_None)) == (((Materials.default__).EC__PUBLIC__KEY__FIELD) in ((pat_let_tv23_).encryptionContext)))) and (not (not(((d_646_suite_).symmetricSignature).is_None)) or ((((pat_let_tv24_).plaintextDataKey).is_Some) == (((pat_let_tv25_).symmetricSigningKey).is_Some)))) and (not (((d_646_suite_).symmetricSignature).is_None) or (((pat_let_tv26_).symmetricSigningKey).is_None))) and (_dafny.quantifier(((pat_let_tv27_).requiredEncryptionContextKeys).UniqueElements, True, lambda39_))
            return iife26_(_pat_let7_0)
        return (AlgorithmSuites.default__.AlgorithmSuite_q((decryptionMaterials).algorithmSuite)) and (iife25_((decryptionMaterials).algorithmSuite))

    @staticmethod
    def DecryptionMaterialsAddDataKey(decryptionMaterials, plaintextDataKey, symmetricSigningKey):
        d_648_suite_ = (decryptionMaterials).algorithmSuite
        d_649_valueOrError0_ = Wrappers.default__.Need(Materials.default__.ValidDecryptionMaterials(decryptionMaterials), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify invalid decryption material.")))
        if (d_649_valueOrError0_).IsFailure():
            return (d_649_valueOrError0_).PropagateFailure()
        elif True:
            d_650_valueOrError1_ = Wrappers.default__.Need(((decryptionMaterials).plaintextDataKey).is_None, software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("Attempt to modify plaintextDataKey.")))
            if (d_650_valueOrError1_).IsFailure():
                return (d_650_valueOrError1_).PropagateFailure()
            elif True:
                d_651_valueOrError2_ = Wrappers.default__.Need((AlgorithmSuites.default__.GetEncryptKeyLength(d_648_suite_)) == (len(plaintextDataKey)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("plaintextDataKey does not match Algorithm Suite specification.")))
                if (d_651_valueOrError2_).IsFailure():
                    return (d_651_valueOrError2_).PropagateFailure()
                elif True:
                    d_652_valueOrError3_ = Wrappers.default__.Need(((symmetricSigningKey).is_Some) == (not((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None)), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key must be added with plaintextDataKey if using an algorithm suite with symmetric signing.")))
                    if (d_652_valueOrError3_).IsFailure():
                        return (d_652_valueOrError3_).PropagateFailure()
                    elif True:
                        d_653_valueOrError4_ = Wrappers.default__.Need(((symmetricSigningKey).is_None) == ((((decryptionMaterials).algorithmSuite).symmetricSignature).is_None), software_amazon_cryptography_materialproviders_internaldafny_types.Error_InvalidDecryptionMaterialsTransition(_dafny.Seq("symmetric signature key cannot be added with plaintextDataKey if using an algorithm suite without symmetric signing.")))
                        if (d_653_valueOrError4_).IsFailure():
                            return (d_653_valueOrError4_).PropagateFailure()
                        elif True:
                            return Wrappers.Result_Success(software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials((decryptionMaterials).algorithmSuite, (decryptionMaterials).encryptionContext, (decryptionMaterials).requiredEncryptionContextKeys, Wrappers.Option_Some(plaintextDataKey), (decryptionMaterials).verificationKey, symmetricSigningKey))

    @staticmethod
    def DecryptionMaterialsWithoutPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_None) and (Materials.default__.ValidDecryptionMaterials(decryptionMaterials))

    @staticmethod
    def DecryptionMaterialsWithPlaintextDataKey(decryptionMaterials):
        return (((decryptionMaterials).plaintextDataKey).is_Some) and (Materials.default__.ValidDecryptionMaterials(decryptionMaterials))

    @_dafny.classproperty
    def EC__PUBLIC__KEY__FIELD(instance):
        d_654_s_ = _dafny.Seq([97, 119, 115, 45, 99, 114, 121, 112, 116, 111, 45, 112, 117, 98, 108, 105, 99, 45, 107, 101, 121])
        return d_654_s_
    @_dafny.classproperty
    def RESERVED__KEY__VALUES(instance):
        return _dafny.Set({(Materials.default__).EC__PUBLIC__KEY__FIELD})

class DecryptionMaterialsPendingPlaintextDataKey:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()()

class SealedDecryptionMaterials:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return software_amazon_cryptography_materialproviders_internaldafny_types.DecryptionMaterials_DecryptionMaterials.default()()
