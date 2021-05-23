# can handle zero division using decorator
def Div_by_zero(func):
    def inner(x, y):
        if y == 0:
            return "Quantity is zero"
        return func(x, y)
    return inner


@Div_by_zero            # declaration
def Unitprice(Amount, Quantity):
    return Amount / Quantity


# Main Program
print(Unitprice(500, 0))
