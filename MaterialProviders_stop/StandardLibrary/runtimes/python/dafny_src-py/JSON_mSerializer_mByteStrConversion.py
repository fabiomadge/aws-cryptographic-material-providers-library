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
import JSON_mUtils_mViews_mCore
import JSON_mUtils_mViews_mWriters
import JSON_mUtils_mViews
import JSON_mUtils_mLexers_mCore
import JSON_mUtils_mLexers_mStrings
import JSON_mUtils_mLexers
import JSON_mUtils_mCursors
import JSON_mUtils_mParsers
import JSON_mUtils_mStr_mCharStrConversion
import JSON_mUtils_mStr_mCharStrEscaping
import JSON_mUtils_mStr
import JSON_mUtils_mSeq
import JSON_mUtils_mVectors
import JSON_mUtils
import JSON_mErrors
import JSON_mValues
import JSON_mSpec
import JSON_mGrammar

assert "JSON_mSerializer_mByteStrConversion" == __name__
JSON_mSerializer_mByteStrConversion = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def Digits(n, base):
        if (n) == (0):
            return _dafny.Seq([])
        elif True:
            d_449_digits_k_ = JSON_mSerializer_mByteStrConversion.default__.Digits(_dafny.euclidian_division(n, base), base)
            d_450_digits_ = (d_449_digits_k_) + (_dafny.Seq([_dafny.euclidian_modulus(n, base)]))
            return d_450_digits_

    @staticmethod
    def OfDigits(digits, chars):
        d_451___accumulator_ = _dafny.Seq([])
        while True:
            with _dafny.label():
                if (digits) == (_dafny.Seq([])):
                    return (d_451___accumulator_) + (_dafny.Seq([]))
                elif True:
                    d_451___accumulator_ = (d_451___accumulator_) + (_dafny.Seq([(chars)[(digits)[0]]]))
                    in103_ = _dafny.Seq((digits)[1::])
                    in104_ = chars
                    digits = in103_
                    chars = in104_
                    raise _dafny.TailCall()
                break

    @staticmethod
    def OfNat__any(n, chars):
        d_452_base_ = len(chars)
        if (n) == (0):
            return _dafny.Seq([(chars)[0]])
        elif True:
            return JSON_mSerializer_mByteStrConversion.default__.OfDigits(JSON_mSerializer_mByteStrConversion.default__.Digits(n, d_452_base_), chars)

    @staticmethod
    def NumberStr(str, minus, is__digit):
        def lambda30_(forall_var_7_):
            d_453_c_: BoundedInts.uint8 = forall_var_7_
            return not ((d_453_c_) in (_dafny.Seq((str)[1::]))) or (is__digit(d_453_c_))

        return not ((str) != (_dafny.Seq([]))) or (((((str)[0]) == (minus)) or (is__digit((str)[0]))) and (_dafny.quantifier((_dafny.Seq((str)[1::])).UniqueElements, True, lambda30_)))

    @staticmethod
    def OfInt__any(n, chars, minus):
        if (n) >= (0):
            return JSON_mSerializer_mByteStrConversion.default__.OfNat__any(n, chars)
        elif True:
            return (_dafny.Seq([minus])) + (JSON_mSerializer_mByteStrConversion.default__.OfNat__any((0) - (n), chars))

    @staticmethod
    def ToNat__any(str, base, digits):
        if (str) == (_dafny.Seq([])):
            return 0
        elif True:
            return ((JSON_mSerializer_mByteStrConversion.default__.ToNat__any(_dafny.Seq((str)[:(len(str)) - (1):]), base, digits)) * (base)) + ((digits)[(str)[(len(str)) - (1)]])

    @staticmethod
    def ToInt__any(str, minus, base, digits):
        if (_dafny.Seq([minus])) <= (str):
            return (0) - (JSON_mSerializer_mByteStrConversion.default__.ToNat__any(_dafny.Seq((str)[1::]), base, digits))
        elif True:
            return JSON_mSerializer_mByteStrConversion.default__.ToNat__any(str, base, digits)

