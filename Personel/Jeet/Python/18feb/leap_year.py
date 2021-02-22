y = int(input('Enter Year:'))
if y % 100 == 0:
    if y % 400 == 0:
        print(f'{y} is leap year')
    else:
        print(f'{y} is not leap year')
else:
    if y % 4 == 0:
        print(f'{y} is leap year')
    else:
        print(f'{y} is not leap year')
