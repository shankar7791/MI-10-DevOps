val= input("Enter the alphabet digit or special character  ")

if val>='65' and val<='90' or val>='97' and val<='122' :
    print(f"{val} is alphabet")
elif val>='0' and val<='9':
    print(f"{val} is Digit")
else :
    print(f"{val} is special character")

