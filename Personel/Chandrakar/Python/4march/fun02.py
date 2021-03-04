from datetime import datetime, timedelta
def aD():
    p_d = datetime(1997, 5, 14)
    n_d = datetime.today() - p_d
    print (n_d.days)

aD() 