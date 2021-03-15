#Remove all duplicates words from a given sentence
 #       Examples:
 #       Input : Geeks for Geeks
  #      Output : Geeks for
    #    Input : Python is great and Java is also great
   #     Output : is also Java Python and great

string = 'nilesh patil nilesh patil nilesh patil'

def duplicate(string):
    output = []
    words= set()
    for word in string.split():
        if word not in words:
            output.append(word)
            words.add(word)
    return ' '.join(output)

print(duplicate(string))
