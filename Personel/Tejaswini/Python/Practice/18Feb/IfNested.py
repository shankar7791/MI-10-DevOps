age = int(input("Enter your age: "))

if age > 21:
    if age > 100:
        print("You are too old, Not allowd...")
    else:
        print(f"Welcome, you are of the right age ie. {age} for Registration")
else:
    print("You are too young, not eligible...")