#fibonace serese using recursion

def fibo(n):
    if n <= 1 :
        return n
    else:
        seq= fibo(n-1) + fibo(n-2)
        return seq
n = int(input("Enter number : "))
for i in range(n):
  print( fibo(i))
