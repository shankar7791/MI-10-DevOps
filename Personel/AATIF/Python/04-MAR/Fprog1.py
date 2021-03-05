def sum_lst() :

    num = int(input("How Many Elements: "))
    lst = []

    for n in range(num) :
        Number = int(input("Enter A Number: "))
        lst.append(Number)
    print("Sum Of the Numbers: ",sum(lst))
sum_lst()