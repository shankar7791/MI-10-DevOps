# define the function for check the given word is  vowel or consonent

def vowelCon ():
  
  letter = str(input("enter the letter to check it is vowel or not : "))

  if (letter=='a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U') :
    print(f"{letter} is a vowel")
  else:
    print(f"{letter} is a consonent")

vowelCon()