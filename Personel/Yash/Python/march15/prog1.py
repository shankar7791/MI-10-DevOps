# Program 1 : Dictionary and counter in Python to find winner of election


from collections import Counter  
  
votes =['a','b','c','a','b','c','a','b','b','a','a','a','c','c','b','c','a','b']  

vote_count=Counter(votes) 

max_votes=max(vote_count.values()) 
  
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes] 

print("Winner of election is : ",sorted(lst)[0]) 
