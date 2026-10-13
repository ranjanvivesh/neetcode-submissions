import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in range(0,len(points)):
            d = points[i][0]*points[i][0] + points[i][1]*points[i][1]
            dist.append(d)
        maxheap = []
        heapq.heapify(maxheap)
        for i in range(0,len(points)):
            heapq.heappush(maxheap,(dist[i],points[i]))
        output = []
        while k != 0 :
            dist,point = heapq.heappop(maxheap)
            output.append(point)
            k -= 1
        return output            