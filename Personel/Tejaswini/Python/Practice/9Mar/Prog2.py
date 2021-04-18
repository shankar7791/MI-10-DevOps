#Write down the names of 10 of your friends in a list and then sort those in alphabetically ascending order.


my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

print("The sorted words are:")
for word in words:
   print(word) 