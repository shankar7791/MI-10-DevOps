# Write a Python function which accepts an arbitrary list and converts it to a heap using Heap queue algorithm.
import heapq as hq
arbitary_heap = [25, 44, 68, 21, 39, 23, 89]
print("arbitary_heap: ", arbitary_heap)
hq.heapify(arbitary_heap)
print("\nHeapify(heap): ", arbitary_heap)