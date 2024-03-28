'''Input: nums = [1,2,3,1,2,3,1,2], k = 2
Output: 6
Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.
It can be shown that there are no good subarrays with length more than 6.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2], k = 1
Output: 2
Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.
It can be shown that there are no good subarrays with length more than 2.
'''
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        d={}
        max1=0
        c=0
        l=0
        for r in range(len(nums)):
            d[nums[r]]=d.get(nums[r],0)+1 
            if d[nums[r]]>k:
                while nums[r]!=nums[l]:
                    d[nums[l]]-=1 
                    l+=1 
                d[nums[r]]-=1 
                l+=1
            max1=max(max1,r-l+1)
        return max1
            
