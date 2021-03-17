#Print anagrams together in Python using List and Dictionary

#Algorithm
#step1 :- create allAnagram function
#step2 :- create empty dictionary
#step3 :- using for loop string value in input
#step4 :- keys values in join and sorted
#step5 :- if condition in key value in dictionary
#step6 :- dictionary append the string value
#step7 :- else part in dictionary and append the dictionary
#step8 :- result the value
#step9 :- using again for loop key value in dictionary items
#step10 :- result the value and join the value of the result
#step11 :- return the result value
#step12 :- create arr in list 
#step13 :- print the arr
#step14 :- allAnagram function in arr



def allAnagrams(input) :
    dict = {}
    for strVal in input :
        key = " ".join(sorted(strVal))

        if key in dict.keys() :
            dict[key].append(strVal)
        else :
            dict[key] = []
            dict[key].append(strVal)

    result = " "
    for key, value in dict.items() :
        result = result + " ".join(value) + " "
    return result

arr = [item for item in input("Enter the list of items :-").split()]
print(arr)
allAnagrams(arr)


