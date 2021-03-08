def triangle(n):
    result = []
    for row in range(n):
        newrow = [1]
        for col in range(1, row+1):
            newcell = newrow[col-1] * float(row+1-col)/col
            newrow.append(int(newcell))
        result.append(newrow)
    return result