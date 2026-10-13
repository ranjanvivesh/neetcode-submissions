import heapq

class Solution:
    def lastStoneWeight(self, stones):
           max_heap = [-num for num in stones]
           heapq.heapify(max_heap)
           while len(max_heap) > 1:
            a = -heapq.heappop(max_heap)
            b = -heapq.heappop(max_heap)
            heapq.heappush(max_heap,-(a-b))
           return -max_heap[0] 