# WAP to accept a word from the user and reverse it.

word = input("Please enter word: ")

word2 = ''
i = len(word) - 1

while(i >= 0):
    word2 = word2 + word[i]
    i = i - 1
    
print("\nThe Original word = ", word)
print("The Reversed word = ", word2)