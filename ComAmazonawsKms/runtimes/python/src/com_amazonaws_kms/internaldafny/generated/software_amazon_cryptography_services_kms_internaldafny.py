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
import DafnyLibraries
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
import FloatCompare
import ConcurrentCall
import Base64
import Base64Lemmas
import Actions
import software_amazon_cryptography_services_kms_internaldafny_types
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

# Module: software_amazon_cryptography_services_kms_internaldafny

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DefaultKMSClientConfigType():
        return KMSClientConfigType_KMSClientConfigType()

    @staticmethod
    def DafnyUserAgentSuffix(runtime):
        d_0_version_ = _dafny.Seq("1.0.1")
        return (((_dafny.Seq("AwsCryptographicMPL/")) + (runtime)) + (_dafny.Seq("/"))) + (d_0_version_)

    @staticmethod
    def CreateSuccessOfClient(client):
        return Wrappers.Result_Success(client)

    @staticmethod
    def CreateFailureOfError(error):
        return Wrappers.Result_Failure(error)


class KMSClientConfigType:
    @_dafny.classproperty
    def AllSingletonConstructors(cls):
        return [KMSClientConfigType_KMSClientConfigType()]
    @classmethod
    def default(cls, ):
        return lambda: KMSClientConfigType_KMSClientConfigType()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_KMSClientConfigType(self) -> bool:
        return isinstance(self, KMSClientConfigType_KMSClientConfigType)

class KMSClientConfigType_KMSClientConfigType(KMSClientConfigType, NamedTuple('KMSClientConfigType', [])):
    def __dafnystr__(self) -> str:
        return f'Kms.KMSClientConfigType.KMSClientConfigType'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, KMSClientConfigType_KMSClientConfigType)
    def __hash__(self) -> int:
        return super().__hash__()

