# orderedDict
from collections import OrderedDict
  
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
  
for key, value in d.items():
    print(key, value)
  
print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
for key, value in od.items():
    print(key, value)




# for defaultDict
from collections import defaultdict
def def_value():
    return "Not Present"
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"])


#NamedTuple
from collections import namedtuple  
Student = namedtuple('Student',['name','age','DOB'])    
S = Student('Nandini','19','2541997')   
print ("The Student age using index is : ")  
print (S[1])    
print ("The Student name using keyname is : ")  
print (S.name)

#ChainMap
from collections import ChainMap        
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 

c = ChainMap(d1, d2, d3)  
       
print(c)