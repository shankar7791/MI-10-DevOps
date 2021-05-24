

def selection(a):
    for i in range(len(a)):
        mini = i
        for j in range(i,len(a)):
            if a[j]<a[i]:
                mini = j
        temp = a[i]
        a[i] = a[mini]
        a[mini] = temp    
a = [4,1,41,59,26,43,59]    
print(f"before selection sortting =  {a} ")
selection(a)

print(f"After selection sortting  =  {a} ")
