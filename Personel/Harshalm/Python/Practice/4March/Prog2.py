#write a function for convert age  to days



age= int(input("Enter the age :-"))

def age_day(num):

    if num > 0 :
        year = 365*num
    return year

print(age_day(age)) 
