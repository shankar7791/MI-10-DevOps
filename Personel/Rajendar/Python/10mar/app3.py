# Program 2 : Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

string1 = input("enter the string : ")
string2 = input("enter the string : ")

a_string = string2[:2] + string1[2:]
b_string = string1[:2] + string2[2:]

print(a_string + ' '+b_string)
