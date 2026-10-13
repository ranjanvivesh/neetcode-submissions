import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Python has a min-heap, so store negatives.
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0