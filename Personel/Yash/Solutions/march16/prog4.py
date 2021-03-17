# Program 4 : Remove all duplicates from a given string in Python 

# def removeDuplicate(str): 
#     s=set(str) 
#     s="".join(s) 
#     print("Without Order:",s) 
#     t="" 
#     for i in str: 
#         if(i in t): 
#             pass
#         else: 
#             t=t+i 
#         print("With Order:",t) 
      
# str="geeksforgeeks"
# removeDuplicate(str) 


str = input("Enter the string : ")
k=""
for i in str :
    if i in k :
        pass
    else :
        k = k + i
print(k)