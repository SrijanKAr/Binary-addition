#function to convert the entered decimal into 8-bits binary number
def BinaryConversion(conversion):
         list=[]
         counter=0
         while counter!=8:
                  remainder=conversion%2
                  list.append(remainder)         #adding remainder value to list
                  conversion=conversion//2
                  counter=counter+1
         return list
