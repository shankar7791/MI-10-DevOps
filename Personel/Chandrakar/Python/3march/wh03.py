#Python program to check whether the string is Symmetrical or Palindrome
def p(c): 
 
  start = 0
  end = len(c)-1
  f = 0
  while(start<end): 
    if (c[start]== c[end]): 
      
      start += 1
      end -= 1
      
    else: 
      f = 1
      break;   
  if f == 0: 
    print("The entered string is palindrome") 
  else: 
    print("The entered string is not palindrome") 
def symm(c): 
  
  l = len(c) 
  flag = 0
  if l%2 == 0: 
    mid = l//2
  else: 
    mid = l//2 + 1 
    
  s1 = 0  
  s2 = mid 
  
  while(s1 < mid and s2 < l): 
    
    if (c[s1] == c[s2]): 
      s1 = s1 + 1
      s2 = s2 + 1
    else: 
      flag = 1
      break
  
  if flag == 0: 
    print("The entered string is symmetrical") 
  else: 
    print("The entered string is not symmetrical") 
c = input("Enter the string: ")
p(c) 
symm(c)