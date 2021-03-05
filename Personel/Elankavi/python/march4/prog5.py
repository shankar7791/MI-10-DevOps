#to print even numbers in a list
def even_num(k):
    even = []
    for n in k:
        if n % 2 == 0:
            even.append(n)
    return even


print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))