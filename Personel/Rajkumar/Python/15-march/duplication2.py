string = str(input("Enter a string:- "));  
   
#Converts the string into lowercase  
str1 = string.lower();  
   
#Split the string into words using built-in function  
w = str1.split(" ");  
   
print("Duplicate words in a given string : ");  
for i in range(0, len(w)):  
    count = 1;  
    for j in range(i+1, len(w)):  
        if(w[i] == (w[j])):  
            count = count + 1;  
            #Set words[j] to 0 to avoid printing visited word  
            w[j] = "0";  
              
    #Displays the duplicate word if count is greater than 1  
    if(count > 1 and w[i] != "0"):  
        print(w[i]);  