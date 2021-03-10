
# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.


def swap(str1, str2):
  swap_1 = str2[:2] + str1[2:]
  swap_2 = str1[:2] + str2[2:]

  return swap_1 + " => " + swap_2
str1 = input("Enter first string : ")
str2 = input("Enter second string : ")
print(swap(str1, str2))



