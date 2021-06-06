from collections import Counter

votes =['Harry','Hermaini','Ron','Hermaini','Harry','Ron', 'Ron','Ron','Harry','Hermaini','Ron','Hermaini','Harry']

vote_count = Counter(votes)

max_votes = max(vote_count.values())

lst = [i for i in vote_count.keys() if vote_count[i]==max_votes]

print("Winner Of the Election: ", sorted(lst)[0])
