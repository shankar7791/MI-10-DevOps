#How to count number of instances of a class in Python?

class count :
    counter = 0
    def __init__(self):
        count.counter += 1
  
obj1 = count()
obj2 = count()
obj3 = count()
obj4 = count()
print(count.counter)