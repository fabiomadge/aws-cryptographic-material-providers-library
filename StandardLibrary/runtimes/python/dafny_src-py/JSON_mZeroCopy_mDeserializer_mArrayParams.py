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
import JSON_mSerializer_mByteStrConversion
import JSON_mSerializer
import JSON_mDeserializer_mUint16StrConversion
import JSON_mDeserializer_mByteStrConversion
import JSON_mDeserializer
import JSON_mConcreteSyntax_mSpec
import JSON_mConcreteSyntax_mSpecProperties
import JSON_mConcreteSyntax
import JSON_mZeroCopy_mSerializer
import JSON_mZeroCopy_mDeserializer_mCore
import JSON_mZeroCopy_mDeserializer_mStrings
import JSON_mZeroCopy_mDeserializer_mNumbers
import JSON_mZeroCopy_mDeserializer_mObjectParams
import JSON_mZeroCopy_mDeserializer_mObjects

# Module: JSON_mZeroCopy_mDeserializer_mArrayParams

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def ElementSpec(t):
        return JSON_mConcreteSyntax_mSpec.default__.Value(t)

    @staticmethod
    def Element(cs, json):
        return (json).fn(cs)

    @_dafny.classproperty
    def OPEN(instance):
        return ord('[')
    @_dafny.classproperty
    def CLOSE(instance):
        return ord(']')
