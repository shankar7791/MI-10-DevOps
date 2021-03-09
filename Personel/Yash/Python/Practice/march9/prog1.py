str = "Hello"
print(type(str))

str1 = 'Hello'  
print(str1)  

str2 = "Hello"  
print(str2)  

str3 = '''
hello 
    guys 
        welcome '''   
print(str3)  

str4 = "Hello"  
print(str4[0])  
print(str4[1])  
print(str4[2])  
print(str4[3])  
print(str4[4])
# print(str4[6])  #IndexError: string index out of range
print()

for x in str4 :
    print(x)
str = "YashMalavade"  
print("Length : ",len(str))
# Start Oth index to end  
print(str[0:])  
# Starts 1th index to 4th index  
print(str[1:5])  
# Starts 2nd index to 3rd index  
print(str[2:4])  
# Starts 0th to 2nd index  
print(str[:3])  
#Starts 4th to 6th index  
print(str[4:7]) 

print()
str = 'YashMalavade'  
print(str[-1])  
print(str[-3]) 
print(str[-2:])  
print(str[-4:-1])  
print(str[-7:-2])  
# Reversing the given string  
print(str[::-1]) 
# print(str[-12])  #IndexError: string index out of range