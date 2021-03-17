#Program to print duplicates from a list of integers

#Algorithm
#step1 :- create the empty list list=[]
#step2 :- create Def function
#step3 :- when create l in length of list
#step4 :- create again empty list1=[]
#step5 :- using for loop i in the range of list l
#step6 :-  k = i + 1
#step7 :- using for loop j in range of k and list l
#step8 :- when list of i is equal to list of j and list of i not in list1
#step9 :- list1 is append in list of i
#step10:- return the value of list1
#step11:- print the duplicate function of list
#step12 :- exit


#Program

list = [int(x) for x in input("Enter the list :-").split()]
def duplicate(list): 
    l = len(list) 
    list1 = [] 
    for i in range(l): 
        k = i + 1
        for j in range(k, l): 
            if list[i] == list[j] and list[i] not in list1: 
                list1.append(list[i]) 
    return list1
  
print(duplicate(list))

