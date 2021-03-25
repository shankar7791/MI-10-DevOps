
# Write a Python class to reverse a string word by word.

class reverse :
    def reverse_words(self, string):
        return " ".join(reversed(string.split()))

obj = reverse()
print(obj.reverse_words("Meerhasan Shaikh"))