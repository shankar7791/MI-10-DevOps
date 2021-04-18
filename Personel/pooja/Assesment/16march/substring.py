def check(string, sub_string):
    if string.find(sub_string) == -1:
        print("no")
    else:
        print("yes")


string = 'my name is pooja'
sub_string = 'pooja'
print(check(string, sub_string))
