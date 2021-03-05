# Program 2 : write a function for convert age to days

from datetime import datetime, timedelta
def ageDays():
    particular_date = datetime(1997, 5, 24)
    new_date = datetime.today() - particular_date
    print (new_date.days)

ageDays()