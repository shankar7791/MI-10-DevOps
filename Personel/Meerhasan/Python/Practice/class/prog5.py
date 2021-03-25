


class reverse :
    
    def __init__(self) :
        self.string = input("Enter a string => ")

        self.rev = self.string[::-1]


obj = reverse()
obj.rev

print("After Reverse => ", obj.rev)