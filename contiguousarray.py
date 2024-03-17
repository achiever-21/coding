class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap={}
        i=0
        max1=0
        countmax=0
        while i<len(nums):
            if nums[i]==1:
                countmax+=1 
            else:
                countmax-=1 
            if countmax==0:
                max1=max(max1,i+1)
            elif countmax in hashmap:
                max1=max(max1,i-hashmap[countmax])
            else:
                hashmap[countmax]=i 
            i+=1
        return max1
        
