# Program 1 : write a menu driven Program to
# Perform following operations
# 1. Length of String
# 2. Reverse String
# 3. Check Palindrome or not
# 4. Check Symmetrical or not
# 5. Check Permutations and combination
# 6. Check two strings are anagram or not
# 7. Exit

def length(str) :
    return len(str)

def reverse(str) :
    return str[::-1]

def palindrome(str) :
    if str == str[::-1] :
        return True
    else :
        return False


def symmetrical(str):       
    n = len(str) 
    flag = 0
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
          
    start1 = 0
    start2 = mid 
      
    while(start1 < mid and start2 < n): 
          
        if (str[start1]== str[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
    if flag == 0: 
        return True
    else: 
        return False

from itertools import permutations
from itertools import combinations

def pc(str):
    p= permutations(str)

    print(f"The permutation of {str} is ")
    for i in list(p):
        print("".join(i),end=" ")

    c=combinations(str,2)
    print(f"\nThe combination of {str} is : ")
    for i in list(c):
        print("".join(i),end =" ")
    print()




def anagram(str1,str2):
    return sorted(str1) == sorted(str2)

print("Select the Menu choice : ")
print("1.Length of String")
print("2.Reverse String")
print("3.Check Palindrome or not")
print("4.Check Symmetrical or not")
print("5.Check Permutations and combination")
print("6.Check two strings are anagram or not")
print("7.Exit")

def operations() :
    while True :    
        choice = input("Enter the choice(1/2/3/4/5/6/7): ")
        if choice in ('1', '2', '3', '4', '5','6','7'):
            if choice == '1':
                str = input("Enter the string : ")
                print("The length of given string is : ",length(str))

            elif choice == '2':
                str = input("Enter the string : ")
                print("The reverse of given string is : ", reverse(str))
            
            elif choice == '3':
                str = input("Enter the string : ")
                if palindrome(str) :
                    print("The given string is palindrome")
                else :
                    print("The given string is not palindrome")

            elif choice == '4':
                str = input("Enter the string : ")
                if symmetrical(str) :
                    print("The given string is symmetrical")
                else :
                    print("The given string is not symmetrical")
                
            elif choice == '5':
                str = input("Enter the string : ")
                print(pc(str))

            elif choice == '6':
                str1 = input("Enter the first string  : ")
                str2 = input("Enter the second string : ")
                if anagram(str1,str2):
                    print("The given strings are anagram")
                else:
                    print("The given strings are not anagram")

            elif choice == '7' :
                print("Good Bye.....")
                exit()
        else:
            print("Invalid Input")
            
        
operations()
