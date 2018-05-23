def recProduct(a,b): #Returns the product of two numbers using recursion

    if b == 0:
        return 0

    if b<0:
        return -a + recProduct(a,b+1)

    if b>0:
        return a + recProduct(a,b-1)

def isPalindrome(string): #Returns whether or not a string is a palindrome using recursion
    stringList = list(string)

    if string == '':
        return True

    if len(stringList) == 1 or len(stringList) == 0:
        return True

    if stringList[0].lower() == stringList[len(stringList)-1].lower(): 
        #Check to make sure each letter at the beginning adn end of the string is the same
        stringList.pop(0)
        stringList.pop(len(stringList)-1)
        return isPalindrome(stringList)

    else:
        return False

    
    
