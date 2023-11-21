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

assert "DafnyLibraries" == __name__
DafnyLibraries = sys.modules[__name__]


class MutableMapTrait:
    pass
    def Put(self, k, v):
        pass

    def Remove(self, k):
        pass


class MutableMap(DafnyLibraries.MutableMapTrait):
    def  __init__(self):
        pass

    def __dafnystr__(self) -> str:
        return "DafnyLibraries.MutableMap"
    def SelectOpt(self, k):
        if (self).HasKey(k):
            return Wrappers.Option_Some((self).Select(k))
        elif True:
            return Wrappers.Option_None()

