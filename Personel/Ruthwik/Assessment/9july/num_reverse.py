# The program takes a number and reverses it.

def rev(n):
    con_str = str(n)
    con_str = list(con_str)
    con_str.reverse()
    con_str = ''.join(con_str)
    rev_num = int(con_str)

    print("Reversed number is: ",rev_num)


num=int(input("Enter number: "))
rev(num)