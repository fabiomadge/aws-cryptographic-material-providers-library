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
import software_amazon_cryptography_services_kms_internaldafny_types
import Relations
import Seq_MergeSort
import Math
import Seq
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
import UUID
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
import software_amazon_cryptography_services_kms_internaldafny
import Com_Amazonaws
import Com
import TestComAmazonawsKms
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

# Module: module_

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Test____Main____(noArgsParameter__):
        d_26_success_: bool
        d_26_success_ = True
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComAmazonawsKms.BasicDecryptTests: ")))
        try:
            if True:
                TestComAmazonawsKms.default__.BasicDecryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_27_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_27_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_26_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComAmazonawsKms.BasicGenerateTests: ")))
        try:
            if True:
                TestComAmazonawsKms.default__.BasicGenerateTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_28_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_28_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_26_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComAmazonawsKms.BasicEncryptTests: ")))
        try:
            if True:
                TestComAmazonawsKms.default__.BasicEncryptTests()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_29_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_29_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_26_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComAmazonawsKms.RegionMatchTest: ")))
        try:
            if True:
                TestComAmazonawsKms.default__.RegionMatchTest()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_30_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_30_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_26_success_ = False
        _dafny.print(_dafny.string_of(_dafny.Seq("TestComAmazonawsKms.EmptyStringIsDefaultRegion: ")))
        try:
            if True:
                TestComAmazonawsKms.default__.EmptyStringIsDefaultRegion()
                if True:
                    _dafny.print(_dafny.string_of(_dafny.Seq("PASSED\n")))
        except _dafny.HaltException as e:
            d_31_haltMessage_ = e.message
            if True:
                _dafny.print(_dafny.string_of(_dafny.Seq("FAILED\n	")))
                _dafny.print(_dafny.string_of(d_31_haltMessage_))
                _dafny.print(_dafny.string_of(_dafny.Seq("\n")))
                d_26_success_ = False
        if not(d_26_success_):
            raise _dafny.HaltException("<stdin>(1,0): " + _dafny.string_of(_dafny.Seq("Test failures occurred: see above.\n")))

