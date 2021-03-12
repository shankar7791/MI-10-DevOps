#Convert list of character into string 

def constr(s):
    str1 = ""
    return str1.join(s)  

t = tuple(input("Enter Tuple : "))
print("Tuple Input : ", t)
print("Tuple to String = ",constr(t)) 
l = list(input("Enter List : "))
print("List Input : ",l)
print("Lsit to String : " , constr(l))