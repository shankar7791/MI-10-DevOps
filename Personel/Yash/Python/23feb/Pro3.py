# Program 3 : Write a Python program that accepts a word from the user and reverse it. 

string = input("Enter the String : ")

temp_str = ''
i = len(string) - 1

while(i >=0):
    temp_str = temp_str + string[i]
    i = i - 1
    
print("The Reversed String is : ",temp_str)