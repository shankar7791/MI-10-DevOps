#Write a Python class to reverse a string word by word
#Input string : 'hello my name is dev'
#Expected Output : '.dev is name my hello'


class reverse:                                #define class
    def reverse_words(self, word):               #define method or create def function
        return ' '.join(reversed(word.split()))   #return the value of reversed function and join or splits the reversed function

str = input("Enter the string :-")           #string

print(reverse().reverse_words(str))    #print the reverse class and reverse_word function in string