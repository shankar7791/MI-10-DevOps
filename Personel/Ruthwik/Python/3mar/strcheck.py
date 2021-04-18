def palindrome(a): 

    str2 = ""

    for i in a:
        str2 = i + str2  

    if(a == str2):
        print("This is a Palindrome String")
    else:
        print("This is Not a Palindrome String")

# Function to check whether the 
# string is symmetrical or not         
def symmetry(a): 
      
    n = len(a) 
    flag = 0
      
    # Check if the string's length 
    # is odd or even 
    if n%2: 
        mid = n//2 +1
    else: 
        mid = n//2
          
    start1 = 0
    start2 = mid 
      
    while(start1 < mid and start2 < n): 
          
        if (a[start1]== a[start2]): 
            start1 = start1 + 1
            start2 = start2 + 1
        else: 
            flag = 1
            break
       
    # Checking the flag variable to  
    # check if the string is symmetrical 
    # or not 
    if flag == 0: 
        print("The entered string is symmetrical") 
    else: 
        print("The entered string is not symmetrical") 
          
# Driver code 
string = input("Enter the string : ")
palindrome(string) 
symmetry(string) 