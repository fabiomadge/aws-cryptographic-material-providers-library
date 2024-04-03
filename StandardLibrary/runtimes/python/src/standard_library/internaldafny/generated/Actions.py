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

# Module: Actions

class default__:
    def  __init__(self):
        pass

    @staticmethod
    def DeterministicMap(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_412_rs_: _dafny.Seq
        d_412_rs_ = _dafny.Seq([])
        hi0_ = len(s)
        for d_413_i_ in range(0, hi0_):
            d_414_r_: TypeVar('R__')
            out16_: TypeVar('R__')
            out16_ = (action).Invoke((s)[d_413_i_])
            d_414_r_ = out16_
            d_412_rs_ = (d_412_rs_) + (_dafny.Seq([d_414_r_]))
        res = d_412_rs_
        return res
        return res

    @staticmethod
    def DeterministicMapWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_415_rs_: _dafny.Seq
        d_415_rs_ = _dafny.Seq([])
        hi1_ = len(s)
        for d_416_i_ in range(0, hi1_):
            d_417_r_: TypeVar('R__')
            d_418_valueOrError0_: Wrappers.Result = None
            out17_: Wrappers.Result
            out17_ = (action).Invoke((s)[d_416_i_])
            d_418_valueOrError0_ = out17_
            if (d_418_valueOrError0_).IsFailure():
                res = (d_418_valueOrError0_).PropagateFailure()
                return res
            d_417_r_ = (d_418_valueOrError0_).Extract()
            d_415_rs_ = (d_415_rs_) + (_dafny.Seq([d_417_r_]))
        res = Wrappers.Result_Success(d_415_rs_)
        return res
        return res

    @staticmethod
    def DeterministicFlatMap(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_419_rs_: _dafny.Seq
        d_419_rs_ = _dafny.Seq([])
        hi2_ = len(s)
        for d_420_i_ in range(0, hi2_):
            d_421_r_: _dafny.Seq
            out18_: _dafny.Seq
            out18_ = (action).Invoke((s)[d_420_i_])
            d_421_r_ = out18_
            d_419_rs_ = (d_419_rs_) + (d_421_r_)
        res = d_419_rs_
        return res
        return res

    @staticmethod
    def DeterministicFlatMapWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_422_rs_: _dafny.Seq
        d_422_rs_ = _dafny.Seq([])
        hi3_ = len(s)
        for d_423_i_ in range(0, hi3_):
            d_424_r_: _dafny.Seq
            d_425_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
            out19_: Wrappers.Result
            out19_ = (action).Invoke((s)[d_423_i_])
            d_425_valueOrError0_ = out19_
            if (d_425_valueOrError0_).IsFailure():
                res = (d_425_valueOrError0_).PropagateFailure()
                return res
            d_424_r_ = (d_425_valueOrError0_).Extract()
            d_422_rs_ = (d_422_rs_) + (d_424_r_)
        rhs4_ = Wrappers.Result_Success(d_422_rs_)
        res = rhs4_
        return res
        return res

    @staticmethod
    def Filter(action, s):
        res: _dafny.Seq = _dafny.Seq({})
        d_426_rs_: _dafny.Seq
        d_426_rs_ = _dafny.Seq([])
        hi4_ = len(s)
        for d_427_i_ in range(0, hi4_):
            d_428_r_: bool
            out20_: bool
            out20_ = (action).Invoke((s)[d_427_i_])
            d_428_r_ = out20_
            if d_428_r_:
                d_426_rs_ = (d_426_rs_) + (_dafny.Seq([(s)[d_427_i_]]))
        res = d_426_rs_
        return res
        return res

    @staticmethod
    def FilterWithResult(action, s):
        res: Wrappers.Result = Wrappers.Result.default(_dafny.Seq)()
        d_429_rs_: _dafny.Seq
        d_429_rs_ = _dafny.Seq([])
        hi5_ = len(s)
        for d_430_i_ in range(0, hi5_):
            d_431_r_: bool
            d_432_valueOrError0_: Wrappers.Result = Wrappers.Result.default(_dafny.defaults.bool)()
            out21_: Wrappers.Result
            out21_ = (action).Invoke((s)[d_430_i_])
            d_432_valueOrError0_ = out21_
            if (d_432_valueOrError0_).IsFailure():
                res = (d_432_valueOrError0_).PropagateFailure()
                return res
            d_431_r_ = (d_432_valueOrError0_).Extract()
            if d_431_r_:
                d_429_rs_ = (d_429_rs_) + (_dafny.Seq([(s)[d_430_i_]]))
        res = Wrappers.Result_Success(d_429_rs_)
        return res
        return res

    @staticmethod
    def ReduceToSuccess(action, s):
        res: Wrappers.Result = None
        d_433_attemptedResults_: _dafny.Seq
        d_433_attemptedResults_ = _dafny.Seq([])
        hi6_ = len(s)
        for d_434_i_ in range(0, hi6_):
            d_435_attempt_: Wrappers.Result
            out22_: Wrappers.Result
            out22_ = (action).Invoke((s)[d_434_i_])
            d_435_attempt_ = out22_
            d_433_attemptedResults_ = (d_433_attemptedResults_) + (_dafny.Seq([d_435_attempt_]))
            if (d_435_attempt_).is_Success:
                rhs5_ = Wrappers.Result_Success((d_435_attempt_).value)
                res = rhs5_
                return res
        res = Wrappers.Result_Failure(Seq.default__.Map(lambda eta0_: default__.pluckErrors(eta0_), d_433_attemptedResults_))
        return res

    @staticmethod
    def pluckErrors(r):
        return (r).error


class ActionInvoke:
    @classmethod
    def default(cls, default_A, default_R):
        return lambda: ActionInvoke_ActionInvoke(default_A(), default_R())
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)
    @property
    def is_ActionInvoke(self) -> bool:
        return isinstance(self, ActionInvoke_ActionInvoke)

class ActionInvoke_ActionInvoke(ActionInvoke, NamedTuple('ActionInvoke', [('input', Any), ('output', Any)])):
    def __dafnystr__(self) -> str:
        return f'Actions.ActionInvoke.ActionInvoke({_dafny.string_of(self.input)}, {_dafny.string_of(self.output)})'
    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ActionInvoke_ActionInvoke) and self.input == __o.input and self.output == __o.output
    def __hash__(self) -> int:
        return super().__hash__()


class Action:
    pass
    def Invoke(self, a):
        pass


class ActionWithResult:
    pass

class DeterministicAction:
    pass
    def Invoke(self, a):
        pass


class DeterministicActionWithResult:
    pass
