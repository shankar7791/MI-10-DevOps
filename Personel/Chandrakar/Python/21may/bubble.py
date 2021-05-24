#  Bubble Sort program
def bubble(a):
    for i in range(len(a)):
        for j in range(i , len(a)-i-1):
            if a[j] > a[j+1] :
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
a  = [5,1,4,2,8]
print(f"before bubble sortting =  {a} ")     
bubble(a)  
print(f"after  bubble sortting =  {a} ")            
    