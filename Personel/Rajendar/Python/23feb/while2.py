
# With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 20:
    i = i + 1
    if i == 10:
        continue
    print(i)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('Current variable value :', var)
print("Good bye!")
