def lsearch(arr, n, x):

    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1


arr = [2,5,8,7,4,6,3]

x = 8

n = len(arr)

res = lsearch( arr, n, x)

if res == -1:
    print('element not found')
else:
    print('element found')