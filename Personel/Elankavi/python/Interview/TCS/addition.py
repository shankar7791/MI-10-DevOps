# Addition of the both the list indices elements and store result in seperate list ?

class addition:
    def __init__(self,l1,l2):
        self.l1=l1
        self.l2=l2
    def adding(self):
        n=[]
        print("List1 : ",self.l1)
        print("List2 : ",self.l2)
        for i in range(0,len(self.l1)):
            n.append(self.l1[i] + self.l2[i])
        return n
b=addition([1, 3, 4, 6, 8],[4, 5, 6, 2, 10])
print("New List : ",b.adding())