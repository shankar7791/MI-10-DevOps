opp = 5
adj = 6
hypo = "x"


if opp == str("x"):
    print("Opposite = " + str(((hypo**2) - (adj**2))**0.5))
elif adj == str("x"):
    print("Adjacent = " + str(((hypo*2) - (opp**2))**0.5))
elif hypo == str("x"):
    print("Hypotenuse = " + str(((opp**2) + (adj**2))**0.5))
else:
    print("not")
