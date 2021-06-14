#Implement DeQue and perform following operations
#a. Insertion at left
#b. Insertion at right
#c. Deletion from left
#d. Deletion from Right
#e. Print
#f. Extend

from collections import deque 
def a_right() :
    values = int(input("enter the right insert values : "))
    d.append(values)
    print(d)
def a_left() :
    values = int(input("enter the left insert values : "))
    d.appendleft(values)
    print(d)
def a_left() :
    values = int(input("enter the left insert values : "))
    d.appendleft(values)
    print(d)
def d_right() :
    d.pop()
    print("After the right value deleting : ",d)    
def d_left() :
    d.popleft()
    print("After the left value deleting : ",d)     
def m_right() :
    value1 = int(input("enter the right insert values : "))
    value2 = int(input("enter the right insert values : "))
    value3 = int(input("enter the right insert values : "))
    d.extend([value1, value2, value3])
    print(d)

d1 = int(input("enter the 1st deque vales is : "))
d2 = int(input("enter the 2nd deque vales is : "))
d3 = int(input("enter the 3rd deque vales is : "))

d = deque([d1, d2, d3])
a_right()
a_left()
d_right()
d_left()
m_right()