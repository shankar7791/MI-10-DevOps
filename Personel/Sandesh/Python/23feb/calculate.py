A = input("Enter the combination: ")
wcount = 0
ncount = 0

ncount = sum(B.isdigit() for B in A)
wcount = sum(B.isalpha() for B in A)
print ("number of letters in the string is", wcount)
print ("number of digits in the string is ", ncount)

