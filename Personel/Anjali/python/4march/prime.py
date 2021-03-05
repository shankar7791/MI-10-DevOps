def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                print("no is not prime")
        print("no is prime")
prime(3)