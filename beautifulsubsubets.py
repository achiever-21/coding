
question: https://leetcode.com/problems/the-number-of-beautiful-subsets/?envType=daily-question&envId=2024-05-23
****Intuition

the problem is to find the count of beautiful subsets form the nums array
beautiful subset
-> absolute difference of any two numbers in the subset is not equal to k.
->then the subset is known as beautifulsubset.

Approach

->this is subset generation problem so we can use recursion and backtracking to generate subsets
->we use choose and not choose general method which we used for other subset generation
->but when we adding our elements into the subset first check whether
nums[i]+k or nums[i]-k not in our ans subset
->when nums[i]+k or nums[i]-k not in subset ,then add this nums[i] into the subset.
->in this problem we just need count of beautiful subsets so at basecase we can increment count as c+=1,when we get beautiful subset from the nums array.
-> at last return count-1 because empty subset also included in our c.

Complexity

Time complexity:
O(2^N)

Space complexity:
O(n)

code:
```
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        prev=[]
        c=0
        index=0
        length=len(nums)
        def r(index):
            nonlocal c
            if length==index:
                c+=1
                return 
            a=nums[index]
#condition for adding elments into the  subset to form as beautifulsubset
            if a+k not in prev and a-k not in prev:
                prev.append(a)
                r(index+1)
                prev.pop()
            r(index+1)
        r(index)
#to remove empty subset decrementing 1
        return c-1
```

            
