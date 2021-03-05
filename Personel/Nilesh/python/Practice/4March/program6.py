#write a function for convert age to days
from datetime import date


def Age(birthDate):
    days_in_year = 365
    age = int((date.today() - birthDate).days / days_in_year)
    return age


print(Age(date(1995, 4, 7)), "years")