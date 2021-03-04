#Convert age into days 
import datetime
def days():
    birth_date = datetime.date(1999, 4, 4)
    curr_date = datetime.date(2021, 3, 4)
    diff = curr_date - birth_date
    print(diff)
    age = diff.days
    return age
print("Your Age in days: ",days())