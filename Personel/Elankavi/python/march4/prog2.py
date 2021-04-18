# program to convert age to days 
import datetime
def days():
    birth_date = datetime.date(1999,10,14)
    current_date = datetime.date(2021, 3, 4)
    diff = current_date - birth_date
    print(diff)
    age = diff.days
    return age
print("Your Age is converted into days: ",days()) 