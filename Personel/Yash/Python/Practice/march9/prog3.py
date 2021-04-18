# Count occurrences of a character in string
str = input("Enter the string : ")
char = input("Enter the charater you want to count : ")
count = 0
for i in str: 
    if i == char: 
        count = count + 1
print (f"The Count of {char} in {str} is {count}") 

counter = str.count(char)
print(f"The Count of {char} in {str} is {counter}")