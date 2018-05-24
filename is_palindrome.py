def isPalindrome(string): #O(n?)
    string = string.lower() #Makes palindrome lowercase to compare strings
    string = string.replace(' ','')
    string1 = string[0:len(string)//2]  #Make string1 first half of string

    #Make string2 second half of string
    if len(string)%2 != 0:
        string2 = string[len(string)//2+1:len(string)+1] 
    else:
        string2 = string[len(string)//2:len(string)+1]

    #Reverse string2
    string2 = string2[::-1]

    #Check if string1 and string2 are equal
    if string1 == string2:
        return True
    else:
        return False

def isPalindrome_norm(string): #O(n/2) -> O(n)
    string = string.lower()  #Make palindrome lowercase
    string = string.replace(' ', '') #Remove all spaces from the string
    if(string=='' or len(string)==1): #Handles special cases
        return True

    for i in range(len(string)//2): #Compares first and last character, excluding middle if odd
        if(string[i] != string[len(string)-i-1]):
            return False
    return True

def isPalindrome_rec(string): #O(n)
    #Returns whether or not a string is a palindrome using recursion
    
    stringList = list(string)

    if string == '' or len(stringList)==1:
        return True

    while ' ' in stringList:
        for item in stringList:
            if ' ' in stringList:
                space = stringList.index(' ')
                stringList.pop(space)

    if stringList[0].lower() == stringList[len(stringList)-1].lower(): 
        #Check to make sure each letter at the beginning adn end of the string is the same
        stringList.pop(0)
        stringList.pop(len(stringList)-1)
        return isPalindrome_rec(stringList)

    else:
        return False
