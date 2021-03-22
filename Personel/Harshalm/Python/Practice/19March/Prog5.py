#Even Number



import array as arr
def mix():
    even = []
    n=int(input("Enter the size of array :-  "))
    for i in range(0,n):
        arr=int(input("Enter the element:- "))
        even.append(arr)
    print(f"Array is {even}")
    for j in range(n):
        if (even[j]%2==0):
            print( "Array is even :-", even[j])

mix()


