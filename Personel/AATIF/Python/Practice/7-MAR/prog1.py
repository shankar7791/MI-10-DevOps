def create_adder(x):
    def adder(y):
        return x+y

    return adder

    add_15 = adder(10)

    print (add_15(10)) 