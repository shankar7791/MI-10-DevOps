def addition(a,b):
    return a+b
def subtr(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b) :
    return a%b
def ex(a,b):
    return a**b
print(" wlecome calculator"  )
print("1. addition")
print("2. subtraction ")
print("3. multiplication ")
print("4. division ")
print("5. modulas ")
print("6. exponet ")
print("select the option 1.....6")    
ch = input("enter the slection : ")
if ch in ('1','2','3','4','5','6'):
    num1= int(input("enter the number: "))
    num2= int(input("enter the number: "))    
    if str == '1':
        print(num1,"+",num2,"=",addition(num1,num2)) 
    elif str =='2':
        print(num1,"-",num2,"=",subtr(num1,num2))    
    elif str == '3':
        print(num1,"*",num2,"=",mult(num1,num2))
    elif str == '4' :
        print(num1,"/",num2,"=",div(num1,num2)) 
    elif str == '5':
        print(num1,"%",num2,"=",mod(num1,num2))  
    else:
        print(num1,"**",num2,"=",ex(num1,num2))   
else:
    print("invaild")          