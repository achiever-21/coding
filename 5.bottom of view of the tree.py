class Solution:
    def bottomView(self, root):
        queue=deque()
        hashmap={}
        ans=[]
        # code here
        h=0
        queue.append([root,h])
        min1=0
        max1=0
        while queue:
            node=queue.popleft()
            root=node[0]
            h=node[1]
            hashmap[h]=root.data
            if root.left:
                queue.append([root.left,h-1])
                min1=min(min1,h-1)
            if root.right:
                queue.append([root.right,h+1])
                hashmap[h+1]=root.right 
                max1=max(max1,h+1)
        for i in range(min1,max1+1):
            ans.append(hashmap[i])
        return ans
