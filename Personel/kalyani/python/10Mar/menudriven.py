
#Program 1 : write a menu driven Program to 
Perform following operations
1. Length of String
2. Reverse String
3. Check Palindrome or not
4. Check Symmetrical or not
5. Check Permutations and combination
6. Check two strings are anagram or not
6. Exit #

str = input("Enter a String: ")
count = 0
for i in str
count = count + 1
print (" length of string is : ")
print(count)


print(" Menu driven program"  )
print("1. length of string")
print("2. reverse of string  ")
print("3. Check Palindrome or not ")
print("4. Check Symmetrical or not ")
print("5. Check Permutations and combination ")
print("6. Check two strings are anagram or not ")
print("6. Exit ")
print("select the option 1.....7") 
str = input("Enter the string : ")
if str in ('1','2','3','4','5','6','7'):   
    if str == '1':111111231111111111111111111
    
    count = 0111111231111
    for i in str
    count = count + 1
    print (" length of string is : ")
    print(count)
    elif str =='2':
        print ( str[-1 :: -1]) 
    elif str == '3':
        b = ( a [-1 :: -1])
        if a == 
        b
        print(" 121312")
    elif str == '4' :
        print(num1,"/",num2,"=",div(num1,num2)) 
    elif str == '5':
        print(num1,"%",num2,"=",mod(num1,num2))  
    else:
        print(num1,"**",num2,"=",ex(num1,num2))   
else:
    print("invaild")
    print("Select the Menu choice : ")
print("1.Length of String")
print("2.Reverse String")
print("3.Check Palindrome or not")
print("4.Check Symmetrical or not")
print("5.Check Permutations and combination")
print("6.Check two strings are anagram or not")
print("7.Exit")

while True :

#Check Length of the string>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def operations() :
        choice = input("Enter the choice(1/2/3/4/5/6/7): ")
        if choice in ('1', '2', '3', '4', '5','6','7'):  

            if choice == '1':
                def strlen(str): 
                    counter = 0    
                    for i in str: 
                        counter += 1
                    return counter 


                str = input("Enter the string to check the length: ")
                print(strlen(str))


#Reverse the given string>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            elif choice == '2':
                def reverse(s): 
                    str = "" 
                    for i in s: 
                        str = i + str
                    return str

                str1 = input("Enter the string to Reverse it: ")

                print ("The original string  is: ",end="") 
                print (str1) 

                print ("The reversed string is: ",end="") 
                print (reverse(str1))

#Check weather the entered string is palindrome or not>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            elif choice == '3':
                def Palinstr(s):
                    return s == s[::-1]


                str1 = input("Enter the string to check palindrome or not: ")
                p = Palinstr(str1)

                if p:
                    print("Yes the entered string is palindrome.")
                else:
                    print("No the entered string is not palindrome.")

#Check weather the entered string is Symmetrical or not>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            elif choice == '4':
                def symstr(str): 
                    l = len(str) 
                    flag = 0

                    if l%2 == 0: 
                        mid = l//2 
                    else: 
                        mid = l//2 + 1 

                    s1 = 0  
                    s2 = mid 

                    while(s1 < mid and s2 < l): 

                        if (str[s1] == str[s2]): 
                            s1 = s1 + 1
                            s2 = s2 + 1
                        else: 
                            flag = 1
                            break

                        if flag == 0: 
                            print("The entered string is symmetrical.") 
                        else: 
                            print("The entered string is not symmetrical.") 
                str = input("Enter the string to check symmetrical or not: ") 
                symstr(str)

#Check the entered string permutations and combinations>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            elif choice == '5':
                import itertools

                str1 = input("Enter the string for permutation: ")

                p = itertools.permutations(str1)

                for val in p:
                    print("Entered string possible permutation: ", *val)

                str2 = input("Enter the string for combinations: ")

                c = itertools.combinations(str2, 2)

                for val in c:
                    print("Entered string Possible Combinations: ", *val)

#Check the two strings entered are anagram or not>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


            elif choice == '6':
                def anastr(str1, str2):

                    if(sorted(str1)== sorted(str2)):
                        print("The strings are anagrams.") 
                    else:
                        print("The strings aren't anagrams.")         

                str1 = input("Enter the string 1: ")
                str2 = input("Enter the string 2: ")
                anastr(str1, str2)

#Exit the Operation>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            elif choice == '7' :
                print("Exit")
        else:
            print("Invalid Input")
            operations()

        while choice == 7 :
            break

    operations() 
13  Personel/AATIF/Python/10-MAR/prog2.py 
@@ -0,0 +1,13 @@
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

a = input("Enter the sring value of a: ")
b = input("Enter the sring value of b: ")

def char_swap(a, b):
  a1 = b[:2] + a[2:]
  b1 = a[:2] + b[2:]

  return a1 + ' ' + b1
print("after swapping the characters of the string: ", char_swap(a, b))           
    