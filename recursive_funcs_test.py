import pytest
from recursive_funcs import *

def test_recProduct_0():
    assert(recProduct(1,5) == 5)

def test_recProduct_1():
    assert(recProduct(-1,5) == -5)

def test_recProduct_2():
    assert(recProduct(-1,-5) == 5)

def test_recProduct_3():
    assert(recProduct(1,-5) == -5)

def test_recProduct_4():
    assert(recProduct(4,5) == 20)

def test_recProduct_5():
    assert(recProduct(0,5) == 0)

def test_isPalindrome_0():
    assert(isPalindrome('RaCeCar') == True)

def test_isPalindrome_1():
    assert(isPalindrome('detartrated') == True)

def test_isPalindrome_2():
    assert(isPalindrome('madam') == True)

def test_isPalindrome_3():
    assert(isPalindrome('octopus') == False)

def test_isPalindrome_4():
    assert(isPalindrome('racecar') == True)

def test_isPalindrome_5():
    assert(isPalindrome('raceCOr') == False)
