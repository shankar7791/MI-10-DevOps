# count the number of vowels in the string 

class vowels:
    
    
    def __init__(self,l):
        
        self.l=l
        
    def count(self,v):
        count1 = 0
        for i in self.l:
            if(i in v):
                count1+=1
        return count1
b=vowels(input("Enter the string : "))
print("No.Of Vowels : ",b.count("'a','e','i','o','u'"))
