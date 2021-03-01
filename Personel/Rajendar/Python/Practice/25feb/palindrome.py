i = 1
while(i > 0):
    n = int(input("Enter the number : "))
    temp = n
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n//10
        sum = temp + rev
        print("sum is : ", sum)
    temp2 = sum
    rev_sum = 0
    while(sum > 0):
        b = sum % 10
        rev_sum = rev_sum * 10 + b
        sum = sum // 10
    print("reverse sum is : ", rev_sum)
    if(temp2 == rev_sum):
        print("palindrome")
        i = 0
    else:
        print("not a palindrome...Again enter the number ")
