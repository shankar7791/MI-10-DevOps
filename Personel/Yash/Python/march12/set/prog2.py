# Program 2 : Check whether a given string is Heterogram or not using set

def heterogram(input): 
    alphabets=[]

    for ch in input :
        if ( ord(ch) >= ord('a') and ord(ch) <= ord('z') ) :
            alphabets.append(ch)
    print(alphabets)
    print(set(alphabets))
   
    if len(set(alphabets))==len(alphabets): 
         print ("Given string is heterogram") 
    else: 
         print ('Given string is not heterogram"') 
  
input = input("Enter the string : ")
heterogram(input) 