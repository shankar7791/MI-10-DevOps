class MyMeta(type) :
    pass

class Myclass(metaclass = MyMeta) :
    pass

class MySubclass(Myclass) :
    pass

print(type(MyMeta))
print(type(Myclass()))
print(type(MySubclass))