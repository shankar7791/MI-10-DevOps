def add(x, y) :  
   
   return x + y 
def subtract(x, y) : 
   
   return x - y 
def modulus(x, y) : 
   
   return x % y 
def division(x, y) : 
     
   return x / y  

def multiplication(x, y) :

   return x * y

def exponent(x, y) :
   return x**y


print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Modulus")  
print("4.Division")  
print("5.Multiplication")
print("6.Exponent")
  
choose = input("Enter Choice => ")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choose == "1" :  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choose == "2" :  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choose == "3":   
   print(num1,"%",num2,"=", modulus(num1,num2))  

elif choose == "4" :  
   print(num1,"/",num2,"=", division(num1,num2))  

elif choose == "5" :
    print(num1,"*",num2,"=", multiplication(num1,num2)) 

elif choose == "6" :
    print(num1,"**",num2,"=", exponent(num1,num2)) 

else :
   print("Invalid Input!!! ")