# Write a Python class to reverse a string word by word.

class reverse:
    def reverse_word(self,r):
        return ' '.join(reversed(r.split()))
b=reverse()
print(b.reverse_word("hi im elankavi"))