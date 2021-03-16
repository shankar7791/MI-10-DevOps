#Dictionary and counter in Python to find winner of election

from collections import Counter 

votes = [item for item in input("Enter the candidates of list items :- ").split()]

vote_count=Counter(votes)     #Count the votes and stores in the dictionary
print("Make Voter Dictionary with Counter:- ",vote_count)
max_votes=max(vote_count.values())     #maximum number of votes 
print("Maximum Count = ",max_votes)
lst=[i for i in vote_count.keys() if vote_count[i] == max_votes]   #Search for people having maximum votes and store in a list 
print("Winner of Election :- ",sorted(lst)[0])  