# With the else statement we can run a block of code once when the condition no longer is true

i = 1
while i < 10:
    print(i)
    i = i+1
else:
    print("i is no longer less than 10")

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
