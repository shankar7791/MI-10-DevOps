# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

a = input("Enter the sring value of a: ")
b = input("Enter the sring value of b: ")

def char_swap(a, b):
  a1 = b[:2] + a[2:]
  b1 = a[:2] + b[2:]

  return a1 + ' ' + b1
print("after swapping the characters of the string: ", char_swap(a, b))