from collections import defaultdict
test_list = ['cat', 'dog', 'tac', 'god', 'act']
print('original list:'+str(test_list))
temp = defaultdict(list)

for ele in test_list:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())

# print result
print("The grouped Anagrams : " + str(res))
