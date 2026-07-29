import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            if i in count:
                count[i] +=1
            else:
                count[i] =1  

        heap=[]
        for n in count:
            heapq.heappush(heap, (count[n], n))
            if len(heap) >k:
                heapq.heappop(heap)
        return [n for freq, n in heap]         
        