class LittleMeta(type):
    def __new__(cls,classname,superclass,attributedict):
        print("classname : ",classname)
        print("superclass : ",superclass)
        print("attributedict : ",attributedict)
        return type.__new__(cls,classname,superclass,attributedict)

class A:
    pass

class B(A, metaclass=LittleMeta):
    pass

class C(B, metaclass=LittleMeta):
    pass

a = A()

