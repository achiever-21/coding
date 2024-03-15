3.Kth Largest Element in an Array 
Time complexity:O(NlogK)
By using sorting the complexity will be O(nlogn)
--------------------------------######################-------------------------
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if heap[0]<num:
                heapq.heappop(heap)
                heapq.heappush(heap,num)  
        return heap[0] 
