import pytest

def sumList(theList): #Returns the sum of a list
    if (theList==[]):
        return 0
    else:
        return theList[0] + sumList(theList[1:]) # [0:] should be [1:]  

def allVowelsA(word): #Finds all of the vowels in word
    if type(word)!=str:
        return False
    result = ''
    vowels = 'aeiouyAEIOUY'
    for i in range(len(word)):
        if word[i] in vowels:
            result+='a'
        else:
            result+=word[i]
    return result

def allVowelsARec(word): #Finding all of the vowels in word using recursion
    if type(word)!=str:
        return False
    if word =='':
        return ""
    vowels = 'aeiouyAEIOUY'
    if word[0] in vowels:
        ch = 'a'
    else:
        ch = word[0]
    return ch + allVowelsARec(word[1:])
