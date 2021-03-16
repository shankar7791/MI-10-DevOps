# Dictionary and counter in python to find winner of election

from collections import Counter
def election():

    from collections import Counter
    votes = ['kavi','elan','kalai','mathi','elan']
    vote_count = Counter(votes)
    max_votes = max(vote_count.values())
    lst = [i for i in vote_count.keys() if vote_count[i] == max_votes]
    print(sorted(lst)[0])
election()
    