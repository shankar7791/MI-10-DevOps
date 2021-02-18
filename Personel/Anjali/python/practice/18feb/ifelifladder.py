marks=int(input("Enter the Markes"))

if marks>75:
    print(f"{marks} pass with distinction")
if marks>65:
    print(f"{marks} pass")
if marks>60:
    print(f"{marks} Second class")
if marks>55:
    print(f"{marks} Higher second class")
if marks<35:
    print(f"{marks} Fail")