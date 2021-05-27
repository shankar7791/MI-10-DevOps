def Bubble_Sort(lst):
    print('\n')
    for i in range(len(lst)):
        if (i+1) == len(lst):
            print(lst)
            return
        if lst[i]>lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
        

l = [5, 8, 2, 9, 4, 3]
for i in range(10):
    Bubble_Sort(l)