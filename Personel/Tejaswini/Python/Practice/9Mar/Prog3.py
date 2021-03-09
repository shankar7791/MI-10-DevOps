#Check whether the substring is present or not

def check(string, sub_str): 
    if (string.find(sub_str) == -1): 
        print("NO") 
    else: 
        print("YES") 
            

string = input("Enter the sring : ")
sub_str = input("Enter sub string : ")
check(string, sub_str) 
