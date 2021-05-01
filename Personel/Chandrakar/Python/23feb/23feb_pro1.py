#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700

x = 1500
while x < 2700:
     x = x + 1
     if x%7==0 and x%5==0:
       
      print(x)