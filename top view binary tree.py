6.top view binary tree 
--------------------------------------------------------------------------------------------------------
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        hashmap=dict()
        ans=[]
        min1,max1=0,0 
        queue=deque()
        queue.append([root,0])
        h=0
        while queue:
            node=queue.popleft()
            root=node[0]
            h=node[1]
            if h not in hashmap:
                hashmap[h]=root.data 
            if root.left:
                queue.append([root.left,h-1])
                min1=min(min1,h-1)
            if root.right:
                queue.append([root.right,h+1])
                max1=max(max1,h+1)
        for i in range(min1,max1+1):
            ans.append(hashmap[i])
        return ans 
