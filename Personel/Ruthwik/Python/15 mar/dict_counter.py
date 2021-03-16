# Dictionary and counter in Python to find winner of election

from collections import Counter  
  
def win(input):  
  
    # convert list of candidates into dictionary  
    # output will be like candidates = {'A':2, 'B':4}  
    votes = Counter(input)  
      
    # create another dictionary and it's key will  
    # be count of votes values will be name of  
    # candidates  
    dict = {}  
  
    for value in votes.values():  
  
        # initialize empty list to each key to  
        # insert candidate names having same  
        # number of votes  
        dict[value] = []  
  
    for (key,value) in votes.items():  
        dict[value].append(key)  
  
    # sort keys in descending order to get maximum  
    # value of votes  
    maxVote = sorted(dict.keys(),reverse=True)[0]  
  
    # check if more than 1 candidates have same  
    # number of votes. If yes, then sort the list  
    # first and print first element  
    if len(dict[maxVote])>1:  
        print (sorted(dict[maxVote])[0]) 
    else:  
        print (dict[maxVote][0])  
  
# Driver program  
# if __name__ == "__main__":  
#     input =['john','johnny','jackie','johnny', 
#             'john','jackie','jamie','jamie', 
#             'john','johnny','jamie','johnny', 
#             'john']  
#     win(input)

n = int(input('Enter number of elements in the list:'))
l = []
for i in range(0, n):
    print("Enter item at index", i )
    item = input()
    l.append(item)
print("User list is ", l)

win(l)