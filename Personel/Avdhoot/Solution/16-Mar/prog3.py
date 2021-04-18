def list(ls1, ls2):
    if (all(x in ls1 for x in ls2)):
        print("Yes Substring is present in Given String")
    else:
        print("No Substring is not present in Given String")

#input
ls1 = "Avdhoot Mane"
ls2 = "Avdhoot"
list(ls1,ls2)
