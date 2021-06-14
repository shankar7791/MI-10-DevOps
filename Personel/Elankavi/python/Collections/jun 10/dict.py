from collections import OrderedDict
from collections import defaultdict
from collections import namedtuple
from collections import ChainMap


def orderedDict(d):
    print("The normal dictionary : \n",d)
    print()
    o = OrderedDict(d)
    print("The Ordered Dictionary : \n",o)

def defaultDict(d):
    print("The input dict : ")
    print(d)
    d = defaultdict(lambda: "Not Present")
    
    print(d["p"])
    print(d["z"])

def default():
    return ("No Values")

def NameTuple():
    name = input("Enter the name of student : ")
    age =  input("Enter the age of student : ")
    DOB = input("Enter the DOB of student : ")
    student = namedtuple('student',['name','age','DOB'])
    s = student(name,age,DOB)
    print("S : ")
    print(s)
    print("The student age using index is : ")
    print(s[1])
    print("The student name using keyname is : ")
    print(s.name)
    print(f"The student age by using keyage : {s.age} and DOB by using index : {s[2]} ")

def chaimap(d):
    d2={}
    n = int(input("Enter the number of values for dict2 : "))
    for i in range(n):
        
        keys = input("Enter the key : ")
        values = input("Enter the value : ")
        d2[keys] = values
    d3={}
    n = int(input("Enter the number of values for dict3 : "))
    for i in range(n):
        
        keys = input("Enter the key : ")
        values = input("Enter the value : ")
        d3[keys] = values
    c = ChainMap(d , d2 , d3)
    print("dict : ",c)
    print("Values : ")
    print(list(c.values()))
    print("Keys " )
    print(list(c.keys()))
# Driver code

while(True):
    print(""" 
    1 -- Order Dict
    2 -- Default Dict
    3 -- Named Tuple
    4 -- Chain map
    5 -- Exit

    """)
    ch = input(("Enter the choice : "))

    if ch == '1':
        d ={}
        n = int(input("Enter the number of values : "))
        for i in range(n):
            keys = input("Enter the key : ")
            values = input("Enter the value : ")
            d[keys] = values
        orderedDict(d)

    elif ch == '2':
        d ={}
        n = int(input("Enter the number of values : "))
        for i in range(n):
            keys = input("Enter the key : ")
            values = input("Enter the value : ")
            d[keys] = values
        defaultDict(d)

    elif ch == '3':
        NameTuple()

    elif ch == '4':
        d ={}
        n = int(input("Enter the number of values : "))
        for i in range(n):
            keys = input("Enter the key : ")
            values = input("Enter the value : ")
            d[keys] = values
        chaimap(d)

    elif ch == '5':
        exit()
    
    else: 
        print("Invalud choice")