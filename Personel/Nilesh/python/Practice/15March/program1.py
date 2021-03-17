#Dictionary and counter in Python to find winner of election

  #input =['john','johnny','jackie','johnny', 
   #         'john','jackie','jamie','jamie', 
    #        'john','johnny','jamie','johnny', 
    #        'john']  
    #winner(input)  
from collections import Counter  
  
def election(names):  
  
    # convert list of candidates into dictionary  
    # output will be likes candidates = {'A':2, 'B':4}  
    votes = Counter(names)  
      
    # create another dictionary and it's key will  
    # be count of votes values will be name of  
    # candidates  
    winner = {}  
  
    for value in votes.values():  
  
        # initialize empty list to each key to  
        # insert candidate names having same  
        # number of votes  
        winner[value] = []  
  
    for (key,value) in votes.items():  
        winner[value].append(key)  
  
    # sort keys in descending order to get maximum  
    # value of votes  
    maxVote = sorted(winner.keys(),reverse=True)[0]  
  
    # check if more than 1 candidates have same  
    # number of votes. If yes, then sort the list  
    # first and print first element  
    if len(winner[maxVote])>1:  
        print (sorted(winner[maxVote])[0]) 
    else:  
        print (winner[maxVote][0])  
  
# Driver program  
if __name__ == "__main__":  
    names =['nil','nilesh','nil','nilesh','nil','kalpesh','tejas','kishan']  
    election(names)  