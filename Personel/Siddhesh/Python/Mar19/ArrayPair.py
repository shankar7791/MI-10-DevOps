 
#Write a Python program to find a pair with highest product from a given array of integers.
def max_pair():

    arr = [11,22,34,56,67,78]

    length = len(arr)

    a = arr[0]
    b = arr[1]

    if length < 2:
        print("no pairs")
    else:
        for i in range (0,length):
            for j in range(i+1,length):
                if arr[i] * arr[j] > a * b:
                    a = arr[i]
                    b = arr[j]
    print(a,b)
max_pair()


