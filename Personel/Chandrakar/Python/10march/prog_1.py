#length of string
def string(st):
    print(f"{st} lenth is : ")
    return len(st)
#revers the string
def strin(st):
    return st[::-1]
#Palindrome or not
def p_drom(st):
    st = st[::-1]
    return st 
#5
from itertools import permutations
from itertools import combinations

def permu_t(a):
    p= permutations(a)

    print(f"\n{a} permutation is ")
    for i in list(p):
        print("".join(i),end=" ")

    c=combinations(a,2)
    print(f"\n\n {a}combination is : ")
    for i in list(c):
        print("".join(i),end =" ")     
#    6
def anagram(st):
    s_st = sorted(st)    
    return s_st
def anagram1(st2) :   
    s_st2 = sorted(st2)
    return s_st2    

op = """1.Length of String
2. Reverse String
3. Check Palindrome or not
4. Check Symmetrical or not
5. Check Permutations and combination
6. Check two strings are anagram or not
7. Exit"""
print(op)
while True:
    ch =input("enter the number selection opration : ")
    if ch in ('1','2','3','4','5','6','7'):   
        if ch == '1':
            print("\t\t1.Length of String".upper())
            str = input("enter the string : ")
            print(string(str))
        elif ch == '2':
            print("Reverse String".upper())
            str = input("enter the string : ")
            print(f"befor the revers is : {str} ")
            print(f"after the reverse : ",strin(str)) 
        elif ch =='3':
            print(" Check Palindrome or not".upper())     
            str = input("enter the string : ")
            if str == p_drom(str) :
                print(str.upper()," is Palindrome string ")
            else:
                print(str.upper()," is not Palindrome  string ")    
        elif ch == '4':
            print("\t\t\tCheck Symmetrical or not".upper())
            str = input("enter the string : ")
            print(f"after the reverse : ",strin(str))
            str1 = (len(strin(str))//2)
            str2 = strin(str)
            s1 =0
            while s1 < str1 and str1 < len(strin(str)):
                if str2[s1]==str2[str1]:
                    print(f"{str} string is Symmetrical")
                    s1+=1
                    str1+=1
                else :
                    print("not")
                break
        elif ch =='5':
            print("\t\t\tCheck Permutations and combination".upper()) 
            a=[]
            n = input("enter the 1st string : ")
            n1 = input("enter the 2nd string : ")
            n2 = input("enter the 3rd string : ")
            a.append(n)
            a.append(n1)
            a.append(n2) 
            print(f"Enter string is : {a}")  
            print(permu_t(a))
        elif ch =='6':
            print("\t\t\tCheck two strings are anagram or not".upper()) 
            str = input("enter the string : ")
            str1 = input("enter the string : ")
            print(anagram(str))
            s = anagram(str)
            s1 = anagram1(str1)
            if s == s1:
                print(f"{str}".upper()," and", f"{str1}".upper()," is anagram string ")
            else :
                print(f"{str}".upper()," and", f"{str1}".upper()," is not anagram string ")   
        else:
            print("Exit")  
    
    else:
        print("invaild") 
    