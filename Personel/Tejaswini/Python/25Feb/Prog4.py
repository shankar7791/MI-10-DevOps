num=int(input("Enter the number :"))
count=num
while True :
    str_num =str(num)
    rev_str=str_num[::-1]
    if str_num==rev_str :
        print(f"{num} is palindrome when entered number is {count}")
        break
    num=int(str_num)+int(rev_str)


