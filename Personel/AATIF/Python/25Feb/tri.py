#Write a Python program to get the third side of right angled triangle from two given sides.

s1 = float(input("Enter the value of side1: "))
s2 = float(input("Enter the value of side2: "))

def fHypotenuse(s1, s2): 
  
    h = (((s1 * s1) + (s2 * s2))**(0.5)); 
    return h;  
  
print(fHypotenuse(s1, s2))