# Python program to find the sum of all items in a dictionary 
def DictSum(inp): 
      
    sum = 0
    for i in inp: 
        sum = sum + inp[i] 
      
    return sum
  
inp1 = {'a': 100, 'b':200, 'c':300} 
inp2 = {'x': 25, 'y':18, 'z':45}
print("Sum of First input: ", DictSum(inp1)) 
print("Sum of Second input: ", DictSum(inp2)) 
