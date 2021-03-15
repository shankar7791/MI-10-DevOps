
# Remove all duplicates words from a given sentence


string = input("Enter a string : ")

def duplicates(string):
    output = []
    seen = set()
    for word in string.split():
        if word not in seen:
            output.append(word)
            seen.add(word)
    return ' '.join(output)

print(duplicates(string))