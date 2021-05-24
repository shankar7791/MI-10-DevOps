arr = [8, 4, 2, 5, 9, 1]

with open('test.txt', 'w') as descending :

    for i in arr :
        descending.write('%s ' %i)

descending.close()

file = open('test.txt','r')

print("Descending Order : \n")
print(file.read(), "\n") 

#----------------------------------------------------------------------------------------------------------------------------------------------------------

new_arr = []

while arr :
    min = arr[0]  
    for x in arr: 
        if x < min:
            min = x
    new_arr.append(min)
    arr.remove(min)    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------

with open ('test.txt', 'w') as ascending :

    for j in new_arr :
        ascending.write('%s ' %j)

ascending.close()

file = open('test.txt','r')

print("Ascending Order : \n")
print(file.read(), "\n")









