# WAP to find function accepts arbitary list and converts it to a heap using heap queue algo.

import heapq as hq

l = [21, 41, 18, 21, 19, 231, 891]
print("original_list : ", l)

h = hq.heapify(l)
print("nHeapify(heap): ", l)