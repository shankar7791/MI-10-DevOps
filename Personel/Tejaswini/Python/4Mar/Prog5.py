#Print even no. from list
List1=[]
n = int(input("Enter the size of list: "))
for i in range( n ):
    num = int(input(f"Enter the element {i+1}: "))        
    List1.append(num) 
print(List1)

def even(List1):
    even_no = [num for num in List1 if num % 2 == 0]
    return even_no
            
print("Even Number from List1: ",even(List1))