#User function Template for python3
class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root):
        # Code here
        ans=[]
        queue=deque()
        queue.append(root)
        while queue:
            node=queue.popleft()
            ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans 


