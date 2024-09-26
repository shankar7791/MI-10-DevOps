from datetime import datetime, timedelta
particular_date = datetime(1993, 4,7)
new_date = datetime.today() - particular_date
print (new_date.days)