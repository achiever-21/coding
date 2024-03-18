# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        level=0
        res=0
        prelevel=0
        prevnum=1
        num=1
        queue.append([root,level,num])
        while queue:
            node,level,num=queue.popleft()
            if level>prelevel:
                prelevel=level 
                prevnum=num 
            res=max(res,num-prevnum+1)
            if node.left:
                queue.append([node.left,level+1,2*num])
            if node.right:
                queue.append([node.right,level+1,2*num+1])
        return res


        
