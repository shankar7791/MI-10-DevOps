
# Algorithm

# 1. Definig a function
# 2. take user input
# 3. Using the conditional statement
# 4. If condition is true execute the if statement
# 5. else execute the else statement
# 6. Return the sum value and print



num = int(input("Enter the last digit : "))

def seq_sum(num) :
    if num <= 0 :
        return num

    else:
        sum = num + seq_sum(num-1)
        return sum

print("The sum is",seq_sum(num))