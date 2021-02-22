inp = input("Enter any Character: ")

if inp>= "a" and inp <= "z" or inp >= "A" and inp<= "Z":
    print(f"The Given Input {inp} is an Alphabet")

elif inp >= "0" and inp <= "9":
    print(f"The Given Input {inp} is a Digit")
else:
    print(f"The Given Character Input {inp} is a Special Character")
elif int(inp) >= 0 and int(inp) <= 9:
    print("The Given Input {inp} is a Digit")
else:
    print("The Given Character Input {inp} is a Special Character")

    print("The Given Character Input {inp} is a Special Character")



