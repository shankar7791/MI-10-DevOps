#Check if Binary representation is Palindrome in Python 

n = int(input('enter no:'))

def d_to_b(n):
    j = bin(n)[2:]
    palin(j)
    
def palin(j):
    print(j == j[::-1])

d_to_b(n)