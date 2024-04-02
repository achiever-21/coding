total no of subsets=2^len(arr)
time complexity:O(2^n)
space complexity:O(2^n)
#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		ans=[]
		sum1=0
		i=0
	    def rec(arr,sum1,ans,i):
		    if i>=N:
                ans.append(sum1)
                return
            rec(arr,sum1+arr[i],ans,i+1)
            rec(arr,sum1,ans,i+1)
        rec(arr,sum1,ans,i)
        return ans
		  
