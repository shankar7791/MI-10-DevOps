#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
i = 1500

while i <= 2700 :
    if (i % 7 == 0) and (i % 5 == 0) :
        print(i)
    i = i + 1
    