class Solution:
    def absolute_diff(self,root):
        min1=100000000000000
        queue=deque()
        ans=[]
        queue.append(root)
        while queue:
            node=queue.popleft()
            ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.sort()
        for i in range(1,len(ans)):
            min1=min(abs(ans[i]-ans[i-1]),min1)
        return min1
