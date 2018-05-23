import pytest

def sum_list(theList): #Returns the sum of a list
    if (theList==[]):
        return 0
    else:
        return theList[0] + sum_list(theList[1:]) # [0:] should be [1:]  
