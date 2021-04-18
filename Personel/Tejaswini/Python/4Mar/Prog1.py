#Sum of all numbers in a list....

List1=[]
n = int(input("Enter the size of list: "))
for i in range( n ):
    num = int(input(f"Enter the element {i+1}: "))        
    List1.append(num)    
def addition(List1):
    sum=0
    for i in List1:
        sum=sum+i
    return sum
print("Addition of list of elements= ",addition(List1))
