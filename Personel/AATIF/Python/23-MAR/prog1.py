class rev_str:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(rev_str().reverse_words('hello my name is dev'))
