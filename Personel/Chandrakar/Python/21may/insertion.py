#insertion sort program
def insertion(a):
    for i in range(1,len(a)):
        j = i 
        while j>0 and a[j-1] > a[j]:
            temp = a[j-1]
            a[j-1] = a[j] 
            a[j]   = temp
            j-=1
a  = [5,1,4,2,8]
print(f"before insertion sortting =  {a} ")     
insertion(a)  
print(f"after  insertion sortting =  {a} ") 