

# Function to reverse words of string
class Reverse:

    def rev_sentence(self, sentence):

        # first split the string into words
        words = sentence.split(' ')

        # then reverse the split string list and join using space
        reverse_sentence = ' '.join(reversed(words))

        # finally return the joined string
        return reverse_sentence


if __name__ == "__main__":
    rev = Reverse()
    print(rev.rev_sentence('hello my name is dev'))
