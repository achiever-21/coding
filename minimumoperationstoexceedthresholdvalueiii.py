 1.Heap related problem (Minimum Operations to Exceed Threshold Value II)
----------------------------------------------------------------------
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        haha=0
        heapq.heapify(nums)
        while len(nums)>=2:
            if nums[0]>=k:
                return haha 
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            heapq.heappush(nums,a*2+b)
            haha+=1 
        return haha
