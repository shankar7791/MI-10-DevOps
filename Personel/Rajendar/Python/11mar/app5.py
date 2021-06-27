# Convert a list of characters into a string
# Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# Output : programming

def convert(s):
    new = ""

    for x in s:
        new += x
    return new


s = ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
print(convert(s))
