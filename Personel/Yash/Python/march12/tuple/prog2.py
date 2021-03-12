# Program 2 : Convert a list of characters into a stringInput : ['p', 'r', 'o', 'g', 'r', 'a', 'm',
#                         'm', 'i', 'n', 'g']
# Output : programming

def convert(s):
    str1 = "" 
    return(str1.join(s)) 


lst = [] 
n = int(input("Enter number of characters : ")) 
for i in range(0, n): 
    ele = input()
    lst.append(ele)

print(convert(lst)) 