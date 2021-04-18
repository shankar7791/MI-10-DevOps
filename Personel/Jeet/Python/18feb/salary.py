sal = int(input('Enter your salary:'))

if sal <= 10000:
    hra = (sal*20)/100
    da = (sal*80)/100
    gs = sal+hra+da
    print('gross sal is:', gs)
elif sal>10000 and sal<=20000:
    hra = (sal*25)/100
    da = (sal*90)/100
    gs = sal+hra+da
    print('gross sal is:', gs)
else:
    hra = (sal*30)/100
    da = (sal*95)/100
    gs = sal+hra+da
    print('gross sal is:', gs)
