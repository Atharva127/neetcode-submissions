class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for n in stones:
            heapq.heappush(max_heap, -n)

        while len(max_heap) > 1:
            y= -heapq.heappop(max_heap)
            x= -heapq.heappop(max_heap)

            if y != x:
                heapq.heappush(max_heap, -(y-x))

        if len(max_heap) ==0:
            return 0
        else:
            return -heapq.heappop(max_heap)                
        