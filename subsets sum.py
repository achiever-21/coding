total no of subsets=2^len(arr)
*BIT MANIPULATION*
	time complexity:O(2^N)*(N)
	space complexity:O(2^N)
	first let us taken an example [2,3,4] for this array total no of subsets is 2^len(arr)=8
		000--> Each time we are selecting only one subarray it a empty sub array
		001-->(4)
		010-->(3)
		011-->(3,4)
		100-->(2)
		101-->(2,4)
		110-->(2,3)
		111-->(2,3,4)
above are total no of subarrays so we have to add each sub array and print 
the code:
for i in range(2**N):
	sum1=0
	for j in range(N):
		if i&(1<<j):
			sum1+=a[i]
	ans.append(sum1)
return ans
		
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
		  
