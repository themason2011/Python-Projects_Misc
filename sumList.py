import pytest

def sumList(theList): #Returns the sum of a list
    if (theList==[]):
        return 0
    else:
        return theList[0] + sumList(theList[1:]) # [0:] should be [1:]  