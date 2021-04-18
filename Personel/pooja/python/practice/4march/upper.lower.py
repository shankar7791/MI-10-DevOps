def string_test(x):
    d = {"upper_case": 0, "lower_case": 0}
    for c in x:
        if c.isupper():
            d["upper_case"] += 1
        elif c.islower():
            d["lower_case"] += 1
        else:
            pass
    print(f"original string", x)
    print("number of uppercase :", d["upper_case"])
    print("number of lower case:", d["lower_case"])


string_test("pooja IS my name FROM Pune")
