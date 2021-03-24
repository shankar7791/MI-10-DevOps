class Rev():
    def Reverse(self, sentence):
        return ' '.join(reversed(sentence.split()))

print(Rev().Reverse("hello my name is dev"))