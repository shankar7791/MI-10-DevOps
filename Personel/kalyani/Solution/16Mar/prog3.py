# check if a substring is present in a given string


string = int(input(" Enter string :"))
sub_string = int(input("Enter word : "))
if ( string.find( sub_string) == -1):
    print(" Substring not found in string :")
else:
    print(" Substring in string :")