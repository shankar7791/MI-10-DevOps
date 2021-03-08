def pascal_triangle(num):
    if num == 0:
        return []
    elif num == 1:
        return[1]
    else:
        row1 = [1]
        row2 = pascal_triangle(num -1)
        for i in range(len(row2)-1) :
            row1 += [1]
    return row1
pascal_triangle(num)

