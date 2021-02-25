A = int(input("Enter a First number : "))
B = int(input("Enter a Second number : "))
def add (A,B) :
    while(B!=0):
        C=A&B
        A=A^B
        B=C<<1
        return A
print("Sum of two numbers : ",add(A,B))