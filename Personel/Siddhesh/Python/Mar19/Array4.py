#Changing and Adding Elements
#Arrays are mutable; their elements can be changed in a similar way as lists.

import array as arr

numbers = arr.array('i',[1, 2, 3, 4, 5, 6 ,10])

#changing first element
numbers[0]=0
print (numbers)


#changing 3rd to 5th element
numbers[2:5] = arr.array('i',[4 ,8 ,9]) 
print(numbers)

#we can add element using append() method
numbers.append(12)
print(numbers)

#we can add element using extennd() method 
numbers.extend([7,9,5])
print(numbers)

#we can add element also using insert() method into array
numbers.insert(7, 13)
print(numbers)

