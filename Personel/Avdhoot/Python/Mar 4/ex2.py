#write a function for convert age to days

import datetime
def days():
    birth_date = datetime.date(1998, 1, 13)
    current_date = datetime.date(2021, 3, 4)
    diff = current_date - birth_date
    print(diff)
    age = diff.days
    return age
print("Your Age is converted into days: ",days())