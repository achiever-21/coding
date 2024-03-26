class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals)<=1:
            return intervals
        stack=[intervals[0]]
        i=1
        while i<len(intervals):
            if stack and stack[-1][1]>=intervals[i][0]:
                stack[-1][-1]=max(intervals[i][-1],stack[-1][-1])
                
            else:
                stack.append(intervals[i])
            i+=1
        return stack
        
