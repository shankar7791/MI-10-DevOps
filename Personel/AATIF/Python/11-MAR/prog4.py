# Python set to check if string is panagram

def check_pangram(a):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(a.lower())) == 0 :
    return True

  return False

str1 = input("Enter a string to check for pangram : ")

if(check_pangram(str1)):
  print("It is a pangram string")
else:
  print("Not a pangram string")