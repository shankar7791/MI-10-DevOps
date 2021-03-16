# Programs 4 : Given a string, find all the duplicate characters which are similar to each others.
# Input : hello  Output : l        
# Input : geeksforgeeeks Output : e g k s

str= input("Enter the string: ")  
   
print("Duplicate characters in a given string: ");  
 
for i in range(0, len(str1)):  
    count = 1;  
    for j in range(i+1, len(str1)):  
        if(str1[i] == str1[j] and str1[i] != ' '):  
            count = count + 1;  
 
            str1 = str1[:j] + '0' + str1[j+1:];  
   
    if(count > 1 and str1[i] != '0'):  
        print(str1[i]);  