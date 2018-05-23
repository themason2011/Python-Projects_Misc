!/usr/bin/env python3

import sys
import convert

if __name__=="__main__":        #Runs what is in here without running what is in the imported files
   print("This is the main block of fToC.py")

   if len(sys.argv) >=2:        #Allows you to type "./lab04.py value" in terminal to directly print the output instead of only using "./lab04.py" and having to run the full program first
       fTempStr = sys.argv[1]
   else:
       fTempStr = input("Please enter a Fahrenheit temperature: ")

   print("You entered: ",fTempStr)

   try:     #Checks if you can convert fTempStr to a float type (returns except part if not)
       fTemp = float(fTempStr)
       cTemp = convert.fToC(fTemp)
       print("{} degrees F = {} degrees C".format(fTemp,cTemp))
   except ValueError:
        print("Sorry, I could not convert {} to a number".format(fTempStr))
