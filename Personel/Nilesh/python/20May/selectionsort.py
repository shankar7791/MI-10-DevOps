def selection(l):
    for i in range(len(l)-1):
        min_index = i 
        for j in range(i+1, len(l)-1):
            if l[j] < l[min_index]:
                min_index = j
    
        l[i], l[min_index] = l[min_index], l[i]

l = []
for i in range(0,5):
    A = int(input())
    l.append(A)
print(l)

selection(l)

print(l)

