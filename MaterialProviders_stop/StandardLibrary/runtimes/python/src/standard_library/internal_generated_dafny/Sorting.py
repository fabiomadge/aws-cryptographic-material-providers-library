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

assert "Sorting" == __name__
Sorting = sys.modules[__name__]

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def LexicographicByteSeqBelow(x, y):
        return Sorting.default__.LexicographicByteSeqBelowAux(x, y, 0)

    @staticmethod
    def LexicographicByteSeqBelowAux(x, y, n):
        return (((n) == (len(x))) or (((n) != (len(y))) and (((x)[n]) < ((y)[n])))) or ((((n) != (len(y))) and (((x)[n]) == ((y)[n]))) and (Sorting.default__.LexicographicByteSeqBelowAux(x, y, (n) + (1))))

    @staticmethod
    def SelectionSort(a, below):
        d_247_m_: int
        d_247_m_ = 0
        while (d_247_m_) < ((a).length(0)):
            d_248_mindex_: int
            d_249_n_: int
            rhs0_: int = d_247_m_
            rhs1_: int = (d_247_m_) + (1)
            d_248_mindex_ = rhs0_
            d_249_n_ = rhs1_
            while (d_249_n_) < ((a).length(0)):
                if not(below((a)[d_248_mindex_], (a)[d_249_n_])):
                    d_248_mindex_ = d_249_n_
                d_249_n_ = (d_249_n_) + (1)
            rhs2_: TypeVar('Data__') = (a)[d_248_mindex_]
            rhs3_: TypeVar('Data__') = (a)[d_247_m_]
            lhs0_: _dafny.Array = a
            lhs1_: int = d_247_m_
            lhs2_: _dafny.Array = a
            lhs3_: int = d_248_mindex_
            lhs0_[lhs1_] = rhs2_
            lhs2_[lhs3_] = rhs3_
            d_247_m_ = (d_247_m_) + (1)

