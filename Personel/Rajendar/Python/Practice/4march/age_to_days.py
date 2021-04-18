from datetime import date


def calAge(birthDate):
    days_in_year = 365
    age = int((date.today() - birthDate).days / days_in_year)
    return age


print(calAge(date(1995, 4, 7)), "years")
