# initializing the list of strings
strings = ["apple", "orange", "grapes", "pear", "peach"]
# initializing an empty dictionary
anagrams = {}
# iterating through the list of strings
for string in strings:
    # sorting the string
    key = "".join(sorted(string))
      # checking whether the key is present in dict or not
       if string in anagrams.keys():
            # appending the original string to the key
            anagrams[key].append(string)
        else:
            # mapping an empty list to the key
            anagrams[key] = []
            # appending the string to the key
            anagrams[key].append(string)
# intializing an empty string
result = ""
# iterating through the dictionary
for key, value in anagrams.items():
    # appending all the values to the result
    result += "".join(value) + " "
# printing the result
print(result)
