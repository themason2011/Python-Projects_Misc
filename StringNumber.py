if __name__=="__main__":

    stopNum1 = False    #Get number 1 through input
    while stopNum1 == False:
        stopNum1 = True
        print("Please enter a number")
        num1AsString = input("First Number: ")

        try:    #Make sure input is an integer
            num1 = int(num1AsString)
        except:
            print("Ooops, that's not a number")
            stopNum1 = False

    stopNum2 = False    #Get number 2 through input
    while stopNum2 == False:
        stopNum2 = True
        print("Please enter another number")
        num2AsString = input("Second number: ")

        try:    #Make sure input is an integer
            num2 = int(num2AsString)
        except:
            print("Ooops, that's not a number")
            stopNum2 = False

    print("You entered: ")
    print("first number=", num1)
    print("second number=", num2)

    print("the sum is: ")   #Print sum of the two numbers
    print(int(num1) + int(num2))
