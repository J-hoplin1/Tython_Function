import pytest
from typing import MutableSequence,Union
from TypedPython.Validators.ParameterValidator import parameter_validator
from TypedPython.Exceptions.Exceptions import *

parameter_validator.config('debug')
pass_phrase = "Pass"

class test():
    def __init__(self):
        pass

    @parameter_validator(int,is_type_method=True)
    def argtest(self,a, *args):
        return pass_phrase

    @parameter_validator(int, int,is_type_method=True, strict_check=False)
    def selective_argtest(self,a, b, c, d, e):
        print(c,d,e)
        return pass_phrase

    @parameter_validator(a=int,b=Union[int,str],c=list,is_type_method=True,strict_check=False)
    def kwargstest(self,a, b, c,*args):
        print(args)
        return pass_phrase

    @parameter_validator()
    def selective_kwargstest(self,**kwargs):
        print(kwargs)
        return pass_phrase


example_insatnce = test()

def test_1():
    '''
    Make type unmatched in argtest make exception
    '''
    with pytest.raises(ParameterTypeUnmatchedException):
        example_insatnce.argtest('str',10,20,30)
def test_2():
    '''
    Make type match in argtest
    '''
    assert example_insatnce.argtest(10,20,30,40,50) == pass_phrase

def test_3():
    '''
    If variadic variable not defined, make exception
    '''
    with pytest.raises(VardictArgmentNotDefined):
        example_insatnce.argtest(10, 20, 30, 40, 50, op=10)

def test_4():
    '''
    without strict check, if type are different with defined in decorator make exception
    '''
    with pytest.raises(ParameterTypeUnmatchedException):
        example_insatnce.selective_argtest('hello',20,30)

def test_5():
    '''
    This decorator only support type
    '''
    with pytest.raises(TypeError):
        example_insatnce.selective_argtest(10, 20)

def test_6():
    '''
    selective args type test
    '''
    assert example_insatnce.selective_argtest(10,20,30,40,50) == pass_phrase

def test_7():
    '''
    kwargs type test
    '''
    assert example_insatnce.kwargstest(10,20,[1,2,3]) == pass_phrase

def test_8():
    '''
    kwargs type test 2
    '''
    assert example_insatnce.kwargstest(10,'str',[1,2,3]) == pass_phrase

def test_9():
    '''
    selective kwargs type test3
    '''
    assert example_insatnce.selective_kwargstest(ex = 10,ex1 = 30) == pass_phrase