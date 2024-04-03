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
import JSON_Utils_Views_Core

# Module: JSON_Utils_Views_Writers


class Chain:
    @classmethod
    def default(cls, ):
        return lambda: Chain_Empty()
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Empty(self) -> bool:
        return isinstance(self, Chain_Empty)
    @property
    def is_Chain(self) -> bool:
        return isinstance(self, Chain_Chain)
    def Length(self):
        d_440___accumulator_ = 0
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (0) + (d_440___accumulator_)
                elif True:
                    d_440___accumulator_ = (((_this).v).Length()) + (d_440___accumulator_)
                    in184_ = (_this).previous
                    _this = in184_
                    
                    raise _dafny.TailCall()
                break

    def Count(self):
        d_441___accumulator_ = 0
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (0) + (d_441___accumulator_)
                elif True:
                    d_441___accumulator_ = (1) + (d_441___accumulator_)
                    in185_ = (_this).previous
                    _this = in185_
                    
                    raise _dafny.TailCall()
                break

    def Bytes(self):
        d_442___accumulator_ = _dafny.Seq([])
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Empty:
                    return (_dafny.Seq([])) + (d_442___accumulator_)
                elif True:
                    d_442___accumulator_ = (((_this).v).Bytes()) + (d_442___accumulator_)
                    in186_ = (_this).previous
                    _this = in186_
                    
                    raise _dafny.TailCall()
                break

    def Append(self, v_k):
        if ((self).is_Chain) and (JSON_Utils_Views_Core.default__.Adjacent((self).v, v_k)):
            return Chain_Chain((self).previous, JSON_Utils_Views_Core.default__.Merge((self).v, v_k))
        elif True:
            return Chain_Chain(self, v_k)

    def CopyTo(self, dest, end):
        _this = self
        while True:
            with _dafny.label():
                if (_this).is_Chain:
                    d_443_end_: int
                    d_443_end_ = (end) - (((_this).v).Length())
                    ((_this).v).CopyTo(dest, d_443_end_)
                    in187_ = (_this).previous
                    in188_ = dest
                    in189_ = d_443_end_
                    _this = in187_
                    
                    dest = in188_
                    end = in189_
                    raise _dafny.TailCall()
                break


class Chain_Empty(Chain, NamedTuple('Empty', [])):
    def __dafnystr__(self) -> str:
        return f'Writers.Chain.Empty'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Chain_Empty)
    def __hash__(self) -> int:
        return super().__hash__()

class Chain_Chain(Chain, NamedTuple('Chain', [('previous', Any), ('v', Any)])):
    def __dafnystr__(self) -> str:
        return f'Writers.Chain.Chain({_dafny.string_of(self.previous)}, {_dafny.string_of(self.v)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Chain_Chain) and self.previous == __o.previous and self.v == __o.v
    def __hash__(self) -> int:
        return super().__hash__()


class Writer:
    def  __init__(self):
        pass

    @staticmethod
    def default():
        return Writer___Writer(0, Chain_Empty())

class Writer__:
    @classmethod
    def default(cls, ):
        return lambda: Writer___Writer(int(0), Chain.default()())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_Writer(self) -> bool:
        return isinstance(self, Writer___Writer)
    def Bytes(self):
        return ((self).chain).Bytes()

    @staticmethod
    def SaturatedAddU32(a, b):
        if (a) <= ((BoundedInts.default__.UINT32__MAX) - (b)):
            return (a) + (b)
        elif True:
            return BoundedInts.default__.UINT32__MAX

    def Append(self, v_k):
        return Writer___Writer(Writer__.SaturatedAddU32((self).length, (v_k).Length()), ((self).chain).Append(v_k))

    def Then(self, fn):
        return fn(self)

    def CopyTo(self, dest):
        ((self).chain).CopyTo(dest, (self).length)

    def ToArray(self):
        bs: _dafny.Array = _dafny.Array(None, 0)
        nw4_ = _dafny.Array(int(0), (self).length)
        bs = nw4_
        (self).CopyTo(bs)
        return bs

    @_dafny.classproperty
    def Empty(instance):
        return Writer___Writer(0, Chain_Empty())
    @property
    def Unsaturated_q(self):
        return ((self).length) != (BoundedInts.default__.UINT32__MAX)
    @property
    def Empty_q(self):
        return ((self).chain).is_Empty

class Writer___Writer(Writer__, NamedTuple('Writer', [('length', Any), ('chain', Any)])):
    def __dafnystr__(self) -> str:
        return f'Writers.Writer_.Writer({_dafny.string_of(self.length)}, {_dafny.string_of(self.chain)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Writer___Writer) and self.length == __o.length and self.chain == __o.chain
    def __hash__(self) -> int:
        return super().__hash__()

