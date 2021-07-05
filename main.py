#importing the function to the main 
import greeting
import validation
import reverse
import binaryAddition
import binaryConversion

greeting.GreetingAtBeginning()            #calling greeting fuction 
#Continuation loop to ask user where he want to continue or not
checkLoop=True
while checkLoop==True:
         
         firstValue=False          #exceptional file handing for the first entered decimal number
         while firstValue==False:
                  try:
                           number1=int(input("Enter the first decimal number:"))
                           number1=validation.validation(number1)     #checking where the number1 is in range or not
                           firstValue=True
                  except:
                           print("Invalid Input!!! Please Re-enter the valid input")
         secondValue=False
         while secondValue==False:         #exceptional file handing for the second entered decimal number
                  try:                
                           number2=int(input("Enter the second decimal number:"))
                           number2=validation.validation(number2)     #checking where the number2 is in range or not
                           secondValue=True
                  except:
                             print("Invalid Input!!! Please Re-enter the valid input")
               #calling the binaryConversion function
         reverse1=binaryConversion.BinaryConversion(number1)  
         reverse2=binaryConversion.BinaryConversion(number2)   
                #calling the reverse function
         first=reverse.ReverseNumber(reverse1)
         #print(type(first))
         second=reverse.ReverseNumber(reverse2)
         #print(type(second))

         SumOfBinaryNumber=binaryAddition.Binaryadder(first,second)          #calling the binaryAddition function
         #print(type(SumOfBinaryNumber))
         print("Binary coversion for first number: ",first)
         print("Binary coversion for second number: ",second)
         print("Adding \n"+first+"\n"+second)
         print("===============================================")
         print("The binary addition is:",SumOfBinaryNumber)
         print("===============================================")

         continuation=input('Do you wish to continue?? Type "No" to exit:')         
         if continuation=="No" or continuation=="no":
                  break
greeting.GreetingAtEnd()    #calling greeting fuction 


