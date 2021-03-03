def alph():
    alpha = (str(input("Enter a Characters : ")))
    if alpha in ("A", "a", "E", "e", "I", "i", "O", "o", "U", "u" ) :
        print (f"{alpha} this is Vowels")
    else :
        print (f"{alpha} this is an consonent")
alph()