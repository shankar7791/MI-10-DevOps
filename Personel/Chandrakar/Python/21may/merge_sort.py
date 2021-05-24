#  Merge Sort program
def merge(a):
    if len(a) > 1:
        mid = len(a)//2
        leftlist = a[:mid]
        right_list =a[mid:]
        merge(leftlist)
        merge(right_list)
        i = 0
        j = 0
        k = 0
        while i< len(leftlist) and j < len(right_list):
            if leftlist[i] < right_list[j]:
                a[k] = leftlist[i]
                i = i + 1
                #k = k + 1
            else:
                a[k] = right_list[j]
                j = j + 1
                #k = k + 1
            k = k + 1    

        while i < len(leftlist):
            a[k] = leftlist[i]
            i = i + 1
            k = k + 1

        while j < len(right_list):
            a[k] = right_list[j]
            j = i + 1
            k = k + 1    
a = [2,4,3,1]
print(f"before merge sortting =  {a} ")     
merge(a)
print(f"after  merge sortting =  {a} ") 

           