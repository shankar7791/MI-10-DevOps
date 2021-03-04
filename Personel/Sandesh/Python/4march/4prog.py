#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters

def letters():
    string = str(input("enter the string : "))

    d={"upper_case":0,"lower_case":0}
    for i in string:
        if i.isupper():
            d["upper_case"] += 1
        else:
            d["lower_case"] +=1
    print("original string : ",string)
    print("count of upper case letters :",d["upper_case"])
    print("count of upper case letters :",d["lower_case"])
letters()
