import heapq

class Solution:
    def lastStoneWeight(self, stones):
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            k = -heapq.heappop(maxheap)
            l = -heapq.heappop(maxheap)
            m = abs(k-l)
            heapq.heappush(maxheap, -m)
        if maxheap:
            return -maxheap[0]
        return 0        

        
            