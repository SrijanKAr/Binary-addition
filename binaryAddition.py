def ORgate(a,b):
       # | is logical OR in python
         return a|b
def ANDgate(a,b):
       # & is logical AND in python
         return a&b
def XORgate(a,b):
         # ^ is logical XOR in python
         return a^b
#function to performed the 8 bits binary addition
def Binaryadder(num1,num2):
         binarySum=[]       #create an emoty list binarySum
         reverseSum=[]      #create an emoty list reverseSum
         carry_in=0
         addition=""          #assign an empty string
         
         for i in range(len(num1)-1,-1,-1):
                  firstBit=int(num1[i])
                  #print(firstBit)
                  secondBit=int(num2[i])
                  #print(secondBit)
                  xor=XORgate(firstBit,secondBit)
                  sum_value=XORgate(xor,carry_in)
                  carry_out=ORgate(ANDgate(firstBit,secondBit),ANDgate(xor,carry_in))
                  carry_in=carry_out
                  reverseSum.append(sum_value)   #add sum value to reverseSum 

         for i in range(len(reverseSum)-1,-1,-1):
                  binarySum.append(reverseSum[i])
                  addition=addition+str(reverseSum[i])  #converting the list into string
         return addition
