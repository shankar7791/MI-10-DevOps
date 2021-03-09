# WAP to reverse the digits of a given number and add it to the original, 
# If the sum is not a palindrome repeat this procedure.

num = int(input("Enter the number: "))

def rev_num(num):

  s = 0
  
  while True:
    d = str(num)
    if d == d[::-1]:
      break
  
    else:
      d1 = int(d[::-1])
      num += d1
      s += 1
  
  return num 

print(rev_num(num))