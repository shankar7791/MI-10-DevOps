# Function to find winner of an election where votes 
from collections import Counter 

votes = [item for item in input("Enter the list items : ").split()]
 
votecount=Counter(votes)     #Count the votes and stores in the dictionary
print("Make Voter Dictionary with Conter: ",votecount)
maxvotes=max(votecount.values())     #maximum number of votes 
print("Maximum Count = ",maxvotes)
lst=[i for i in votecount.keys() if votecount[i]==maxvotes]   #Search for people having maximum votes and store in a list 
print("Winner of Election : ",sorted(lst)[0])         

