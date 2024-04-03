import sys
from typing import Callable, Any, TypeVar, NamedTuple
from math import floor
from itertools import count

import module_
import _dafny
import System_
import Wrappers
import Relations
import Seq_MergeSort
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
import StandardLibraryInterop
import StandardLibrary_UInt
import StandardLibrary_String
import StandardLibrary
import UUID
import UTF8
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
import JSON_Utils_Views_Core
import JSON_Utils_Views_Writers
import JSON_Utils_Views
import JSON_Utils_Lexers_Core
import JSON_Utils_Lexers_Strings
import JSON_Utils_Lexers
import JSON_Utils_Cursors
import JSON_Utils_Parsers
import JSON_Utils_Str_CharStrConversion
import JSON_Utils_Str_CharStrEscaping
import JSON_Utils_Str
import JSON_Utils_Seq
import JSON_Utils_Vectors
import JSON_Utils
import JSON_Errors
import JSON_Values
import JSON_Spec
import JSON_Grammar
import JSON_Serializer_ByteStrConversion
import JSON_Serializer
import JSON_Deserializer_Uint16StrConversion
import JSON_Deserializer_ByteStrConversion
import JSON_Deserializer
import JSON_ConcreteSyntax_Spec
import JSON_ConcreteSyntax_SpecProperties
import JSON_ConcreteSyntax
import JSON_ZeroCopy_Serializer
import JSON_ZeroCopy_Deserializer_Core
import JSON_ZeroCopy_Deserializer_Strings
import JSON_ZeroCopy_Deserializer_Numbers
import JSON_ZeroCopy_Deserializer_ObjectParams
import JSON_ZeroCopy_Deserializer_Objects
import JSON_ZeroCopy_Deserializer_ArrayParams
import JSON_ZeroCopy_Deserializer_Arrays
import JSON_ZeroCopy_Deserializer_Constants
import JSON_ZeroCopy_Deserializer_Values
import JSON_ZeroCopy_Deserializer_API
import JSON_ZeroCopy_Deserializer
import JSON_ZeroCopy_API
import JSON_ZeroCopy
import JSON_API
import JSON

# Module: software_amazon_cryptography_primitives_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultCryptoConfig():
        return software_amazon_cryptography_primitives_internaldafny_types.CryptoConfig_CryptoConfig()

    @staticmethod
    def AtomicPrimitives(config):
        res: Wrappers.Result = None
        d_111_client_: AtomicPrimitivesClient
        nw0_ = AtomicPrimitivesClient()
        nw0_.ctor__(AwsCryptographyPrimitivesOperations.Config_Config())
        d_111_client_ = nw0_
        res = Wrappers.Result_Success(d_111_client_)
        return res
        return res

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class AtomicPrimitivesClient(software_amazon_cryptography_primitives_internaldafny_types.IAwsCryptographicPrimitivesClient):
    def  __init__(self):
        self._config: AwsCryptographyPrimitivesOperations.Config = AwsCryptographyPrimitivesOperations.Config.default()()
        pass

    def __dafnystr__(self) -> str:
        return "Aws.Cryptography.Primitives.AtomicPrimitivesClient"
    def ctor__(self, config):
        (self)._config = config

    def GenerateRandomBytes(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out36_: Wrappers.Result
        out36_ = AwsCryptographyPrimitivesOperations.default__.GenerateRandomBytes((self).config, input)
        output = out36_
        return output

    def Digest(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out37_: Wrappers.Result
        out37_ = AwsCryptographyPrimitivesOperations.default__.Digest((self).config, input)
        output = out37_
        return output

    def HMac(self, input):
        return AwsCryptographyPrimitivesOperations.default__.HMac((self).config, input)

    def HkdfExtract(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out38_: Wrappers.Result
        out38_ = AwsCryptographyPrimitivesOperations.default__.HkdfExtract((self).config, input)
        output = out38_
        return output

    def HkdfExpand(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out39_: Wrappers.Result
        out39_ = AwsCryptographyPrimitivesOperations.default__.HkdfExpand((self).config, input)
        output = out39_
        return output

    def Hkdf(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out40_: Wrappers.Result
        out40_ = AwsCryptographyPrimitivesOperations.default__.Hkdf((self).config, input)
        output = out40_
        return output

    def KdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out41_: Wrappers.Result
        out41_ = AwsCryptographyPrimitivesOperations.default__.KdfCounterMode((self).config, input)
        output = out41_
        return output

    def AesKdfCounterMode(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out42_: Wrappers.Result
        out42_ = AwsCryptographyPrimitivesOperations.default__.AesKdfCounterMode((self).config, input)
        output = out42_
        return output

    def AESEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.AESEncryptOutput.default())()
        out43_: Wrappers.Result
        out43_ = AwsCryptographyPrimitivesOperations.default__.AESEncrypt((self).config, input)
        output = out43_
        return output

    def AESDecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out44_: Wrappers.Result
        out44_ = AwsCryptographyPrimitivesOperations.default__.AESDecrypt((self).config, input)
        output = out44_
        return output

    def GenerateRSAKeyPair(self, input):
        output: Wrappers.Result = None
        out45_: Wrappers.Result
        out45_ = AwsCryptographyPrimitivesOperations.default__.GenerateRSAKeyPair((self).config, input)
        output = out45_
        return output

    def GetRSAKeyModulusLength(self, input):
        return AwsCryptographyPrimitivesOperations.default__.GetRSAKeyModulusLength((self).config, input)

    def RSADecrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out46_: Wrappers.Result
        out46_ = AwsCryptographyPrimitivesOperations.default__.RSADecrypt((self).config, input)
        output = out46_
        return output

    def RSAEncrypt(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out47_: Wrappers.Result
        out47_ = AwsCryptographyPrimitivesOperations.default__.RSAEncrypt((self).config, input)
        output = out47_
        return output

    def GenerateECDSASignatureKey(self, input):
        output: Wrappers.Result = Wrappers.Result.default(software_amazon_cryptography_primitives_internaldafny_types.GenerateECDSASignatureKeyOutput.default())()
        out48_: Wrappers.Result
        out48_ = AwsCryptographyPrimitivesOperations.default__.GenerateECDSASignatureKey((self).config, input)
        output = out48_
        return output

    def ECDSASign(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        out49_: Wrappers.Result
        out49_ = AwsCryptographyPrimitivesOperations.default__.ECDSASign((self).config, input)
        output = out49_
        return output

    def ECDSAVerify(self, input):
        output: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
        out50_: Wrappers.Result
        out50_ = AwsCryptographyPrimitivesOperations.default__.ECDSAVerify((self).config, input)
        output = out50_
        return output

    @property
    def config(self):
        return self._config
