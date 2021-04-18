#write a function for convert age to days

age=int(input('enter age'))

def age_day(n):

    if n>0:
        c = 365*n
    return c

print (age_day(age))