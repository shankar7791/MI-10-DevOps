
# check palindrome using class


class palimdrome :

    def __init__(self) :
        self.string = input("Enter a string => ")
        self.rev = self.string[::-1]


    def check(self) :
        if self.string == self.rev :
            print("string is Palindrome")

        else :
            print("String is not a Palindrome ")


obj = palimdrome()
obj.check()



