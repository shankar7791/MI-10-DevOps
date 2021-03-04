#Python function that accepts a string and calculate the number of upper case letters and lower case letters.

str=input("Enter the string : ")
def string_test(s):
    d={"uc":0, "lc":0}
    for c in s:
        if c.isupper():
           d["uc"]+=1
        elif c.islower():
           d["lc"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["uc"])
    print ("No. of Lower case Characters : ", d["lc"])

string_test(str)