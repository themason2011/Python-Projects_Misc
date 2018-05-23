#!/usr/bin/env python3

import sys
import pytest

# Mason Corey, Fall 2017

def createWordList(filename):
    '''
    Reads in the in the filename and creates a list L which contains all the words. 
    You must remove the newline character ('\n') at the end of each word.  
    :param filename: the string which represents the filename you are reading from.
    :return: A list of strings  
    '''

    if filename == '' or type(filename)!=str:
        return False

    L = []

    file = open(filename)

    line = file.readline()

    L.append(line[:-1])

    for line in file:
        L.append(line[:-1])

    return L


def canWeMakeIt(myWord, myLetters):

    '''
    Takes in a word and a string of letters and checks whether the word can be made with those letters.  
    :param myWord: the string we are checking.
    :param myLetters: a string of letters we can use to build a string. 
    :return: A bool whether the string can be made or not.  
    '''

    myList = []

    for item in myLetters:
        myList.append(item)

    for i in range(len(myWord)):
        if myWord[i] not in myList:
            return False

        index = myList.index(myWord[i])

        myList.pop(index)
    
    return True

def getWordPoints(myWord, letterPoints):
	
    '''
    Returns the total points of a given word. 
    :param myWord: the string you want to calculate points for
    :param LetterPoints: a dictionary of (letter, value) pairs which gives the point value of each letter
    :return: The total point value of the word.   
    '''

    dict_points = {
        'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,
        'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,
        'w':4,'x':8,'y':4,'z':10}

    numPoints = 0

    for item in myWord:
        numPoints += letterPoints.get(item,0)
        
    return numPoints

def outputWordPointPairs(pointWordList, myLetters, toFile):
    '''
    Outputs the contents of pointWordList in a specified format to the terminal 
    or a file.
		
    :param pointWordList: a list of tuples to output to, with each tuple 
     containing a (pointValue, word) pair
    :param myLetters: a string that you will name the file with if toFile is True
    :param toFile: a boolean to decide whether I want to print to file or not. If True then output to file else output to terminal.  
    :return: None
    '''

    width = len(myLetters)+4

    if toFile == True:
        #write possible pointValue,word to text file

        file = open(myLetters + '.txt','w')

        for i in range(len(pointWordList)):

            lenSpace = width - len(pointWordList[i][1])
            file.write(pointWordList[i][1] + ' '*lenSpace + str(pointWordList[i][0]) + '\n')

        file.close()

    if toFile == False:
        #print values to python shell

        for i in range(len(pointWordList)):

            lenSpace = width - len(pointWordList[i][1])
            print(pointWordList[i][1] + ' '*lenSpace + str(pointWordList[i][0]) + '\n',end = '')

    return
        
def scrabbleWords(myLetters):
    '''
    A function which takes in a string of letters and shows what words can be constructed from it.
    It should use the helper functions defined above to do so. 
    :param myLetters: a string of letters we are using. 
    :return: None
    '''

    letterPoints = {
        'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,
        'l':1,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,
        'w':4,'x':8,'y':4,'z':10}

    myWords = []
    
    wordList = createWordList('wordlist.txt')

    for item in wordList:
        if canWeMakeIt(item,myLetters)==True:
            myWords.append(item)

    pointWordList = []

    for word in myWords:
        pointValue = getWordPoints(word, letterPoints)
        pointWordList.append((pointValue, word))

    pointWordList.sort(reverse = True)

    outputWordPointPairs(pointWordList, myLetters, False)
    outputWordPointPairs(pointWordList, myLetters, True)

    return

if __name__=="__main__":
  if len(sys.argv) >= 2:
  	scrabbleWords(sys.argv[1])
  else:
  	print("Invalid input, please try again")
