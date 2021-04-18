# Check whether a given string is Heterogram or not


def isHeterogram(s, n): 
    hash = [0] * 26

    for i in range(n): 
           
        if s[i] != ' ': 
               
            if hash[ord(s[i]) - ord('a')] == 0: 
                hash[ord(s[i]) - ord('a')] = 1
               
            else: 
                return False
      
    return True

s = input("Enter the String to check heterogram:")
n = len(s) 
  
print("YES" if isHeterogram(s, n) else "NO")