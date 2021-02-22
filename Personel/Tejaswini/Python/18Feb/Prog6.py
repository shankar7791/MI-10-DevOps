inp = input("Enter any Character: ")

if inp>= "a" and inp <= "z" or inp >= "A" and inp<= "Z":
    print(f"The Given Input {inp} is an Alphabet")

elif inp >= "0" and inp <= "9":
    print(f"The Given Input {inp} is a Digit")
else:
    print(f"The Given Character Input {inp} is a Special Character")