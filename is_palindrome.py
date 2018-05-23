def is_palindrome(string): 
    string = string.lower() #Makes palindrome lowercase to compare strings
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
