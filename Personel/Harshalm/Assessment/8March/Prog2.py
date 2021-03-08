#Check if Binary representation is Palindrome in Python 

def palindrome(x,k) :
    if((x &(1 << (k-1))) !=0) :
        return True
    else:
        return False

def palindrome1(x):
    l = 1
    r = 2 * 8
    
    while (l < r) :
        if (palindrome(x,1) != palindrome(x,r)):
            return False
        l += 1
        r -= 1
    return True

    