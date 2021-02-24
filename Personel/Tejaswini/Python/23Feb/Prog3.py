word1 = input("Enter the Word: ")
word2 = ''

i=len(word1)-1

while i>=0:
    word2 = word2+word1[i]
    i = i-1

print(f"The Original String is --> {word1}")
print(f"\nThe Resverse String is --> {word2}")