#Write a Python function to check whether a string is a pangram or not
str1 ="i live in bhilai"
ab  = "abcdefg"
def pang():
    flag = True 
    for char in ab:
        if char not in str1.lower():
            flag = False
    if (flag==True):
        print("Pangram")
    else:
        print("not panram")            
pang()        