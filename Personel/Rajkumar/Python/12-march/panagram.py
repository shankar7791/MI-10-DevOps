#Python set to check if string is panagram
def pangram(arg):
    if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0 :
        return True
    else:
        return False

str = input("Enter a string to check for pangram : ")

if(pangram(str)):
  print("It is a pangram string")
else:
  print("Not a pangram string")