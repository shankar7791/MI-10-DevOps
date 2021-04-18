class reverse:
    def reverse_word(self, s):
        return ' '.join(reversed(s.split()))


print(reverse().reverse_word('my  name  is   pooja'))
