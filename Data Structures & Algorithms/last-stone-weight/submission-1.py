import heapq

class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            a = stones[-1]
            stones.pop()
            b = stones[-1]
            stones.pop()
            stones.append(abs(a-b))
        return stones[0]    