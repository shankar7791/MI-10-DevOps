
def swap(a,b):
    f_char = first_string[0:2]
    s_char = second_string[0:2]
    new_string = s_char + first_string[-1]
    new_string2 = f_char + second_string[-1]
    return new_string ,new_string2
     
first_string = "abc"
second_string = "xyz"
print(f"before swapping :'abc' and 'xyz' ")
print(f"after swapping : ",swap(first_string,second_string))