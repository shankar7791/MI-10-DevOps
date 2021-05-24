#  Write a python program to reverse a string word by word.


class reverse:
     def reverse_words(self,s):
        return ''.join (reversed(s.split()))
print(reverse().reverse_words(' hello my name is dev'))
