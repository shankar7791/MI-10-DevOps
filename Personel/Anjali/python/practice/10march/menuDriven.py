def length(string):
    print(len(string))

def reverse(string):
    print(string[::-1])

def palindrom(string):
    str=''
    i=(len(string))-1
    while i>=0:
        str=str+string[i]
        i=i-1
    print(str)
    if string==str:
        print(f"String is palindrom {string}")
    else:
        print(f"String is not palindrom {string}")
def symmetrical(string):
    n=len(string)
    flag=0
    if n%2:
        mid=n//2+1
    else:
        mid=n//2
    start=0
    start1=mid

    while(start<mid and start1<n):
        if (string[start]== string[start1]): 
            start = start + 1
            start1 = start1 + 1
        else:
            flag=1
            break
    if flag == 0: 
        print(f"String is symmetrical {string}") 
    else: 
        print(f"String is not symmetrical {string}")

def anagram(str1,str2):
    str1=input("Enter the string1   ")
    str2=input("Enter the string2   ")
    if(sorted(str1)==sorted(str2)):
        print("String are anagram")
    else:
        print("String are not anagram")

def exit():
    print(exit)
    exit()

ch=input("""
1.Length of string
2.Revers String
3.Check Palindrom or not
4.Check Symmetrical or not
5.Check Two String are Anagram or not
6.exit
Enter Your Choice""")

while True:
    if ch=='1':
        string=input("Enter the string  ")
        length(string)
    elif ch=='2':
        string=input("Enter the string  ")

        reverse(string)
    elif ch=='3':
        string=input("Enter the string  ")

        palindrom(string)
    elif ch=='4':
        string=input("Enter the string  ")

        symmetrical(string)
    elif ch=='5':
        str1=input("Enter the string  ")
        str2=input("Enter the string  ")

        anagram(str1,str2)
    elif ch=='6':
        exit()
        break
    else:
        print("Invalid Choice")
