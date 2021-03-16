#Dictionary and counter in Python to find winner of election
votes = ['Giggs', 'Giggs', 'Greg', 'Joan', 'Jenny', 'Jenny', 'Jenny', 'Jones']


from collections import Counter
top = Counter(votes).most_common(1)

winner, top_votes = top[0]
print('{} won with {} votes.'.format(winner, top_votes))