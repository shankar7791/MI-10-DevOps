
# Program 1 : write a menu driven Program to
# Perform following operations
# 1. Length of String
# 2. Reverse String
# 3. Check Palindrome or not
# 4. Check Symmetrical or not
# 5. Check Permutations and combination
# 6. Check two strings are anagram or not
# 6. Exit




# str = input("Enter a string : ")
def lenth(str) :
    return len(str)

def rev(str) :

    reverse = str[::-1]

    return reverse

def palindrome(str) :
    reverse = str[::-1]
    if reverse == str :
        print(f"String {str} is palindrome")
        return reverse
    else :
        print(f"String {str} is not a palindrome")      
        return reverse

def Symmetrical(str): 
      
    n = len(str) 
    flag = 0
    
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
          
    start1 = 0
    start2 = mid 
      
    while (start1 < mid and start2 < n): 
          
        if (str[start1] == str[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
       
    if flag == 0: 
        print(f"The entered string {str} is symmetrical") 
    else: 
        print(f"The entered string {str} is not symmetrical") 


import itertools
def permutation(str) :

    per = itertools.permutations(str)

    for val in per:     
        print(*val)
    
    com = itertools.combinations(str, 2)
    
    for val in com:    
        print(*val)


def anagram(str, s2):

	if(sorted(str)== sorted(s2)):
		print("The strings are anagrams.") 
	else:
		print("The strings aren't anagrams.")		 
		
    

print(""" Operations 
1. Check the lenth of a string
2. Reverse the string 
3. Check string is palindrom or not 
4. Check string is symentric or not
5. Chech permutation and conbination 
6. Check string are anagram or not 
7. Exit """)

while True :
    print("")

    check = input("Choose Your Operation => ")


    if check == "1" :
        str = input("Enter a string : ")
        print("The lenth of a string is : ",lenth(str))

    elif check == "2" :
        str = input("Enter a string : ")
        print("Reverse of the string : ",rev(str))

    elif check == "3" :
        str = input("Enter a string : ")
        palindrome(str)

    elif check == "4" :
        str = input("Enter a string : ")
        Symmetrical(str)

    elif check == "5" :
        str = input("Enter a string : ")
        permutation(str)

    elif check == "6" :
        str = input("Enter a string : ")
        s2 = input("enter second string : ")
        anagram(str, s2)
    elif check == "7" :
        break
        print("")
        
    else :
        print("Enter a valid input !!!!  ")

