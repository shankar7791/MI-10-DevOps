import re 

text = str(input("Enter the sentence : "))
print("Your sentence : ",text)
res = len(re.findall(r'\w+', text))
print("count : ",res)
