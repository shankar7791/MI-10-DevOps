def func(k):
    if(k > 0):
        result = k + func(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
func(6)
