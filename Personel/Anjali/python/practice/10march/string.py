string1 = input("enter the string : ")
string2 = input("enter the string : ")

a_string = string2[:2] + string1[2:]
b_string = string1[:2] + string2[2:]

print(a_string +' '+b_string) 