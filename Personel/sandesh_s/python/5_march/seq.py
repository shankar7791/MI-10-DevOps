#find sum of seq using recursion

num = int(input("Enter the last digit : "))

def seq_sum(num) :
    if num <= 0 :
        return num

    else:
        sum = num + seq_sum(num-1)
        return sum

print("The sum is",seq_sum(num))
