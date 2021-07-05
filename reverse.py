#creating function ReverseNumber
def ReverseNumber(RevNum):
         SecondList=[]      #assign an empty list as SecondList
         BinStr=""           #assign an empty string as BinStr
         for i in range(len(RevNum)-1,-1,-1):
                 SecondList.append(RevNum[i])    #add the RevNum to SecondList
                 BinStr=BinStr+str(RevNum[i])    #converting the list into string 
         return BinStr
