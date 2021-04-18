# Programs 4 : Given a string, find all the duplicate characters which are similar to each others.
#         Input : hello
#         Output : l        Input : geeksforgeeeks
#         Output : e g k s



from collections import Counter

def find_duplicates(s):
    elements = Counter(s)
    return [k for k,v in elements.items() if v>1]

  
inp = input("Enter the string : ")

print(find_duplicates(inp))
