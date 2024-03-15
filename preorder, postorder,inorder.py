class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

def getTreeTraversal(root):
    # Write your code here.
    arr1=[]
    arr2=[]
    arr3=[]
    if root is None:
        return []
    inorder(root,arr1)
    preorder(root,arr2)
    postorder(root,arr3)
    return [arr1,arr2,arr3]
def inorder(root,arr):
    if root is None:
        return 
    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)
    return arr
def preorder(root,arr):
    if root is None:
        return 
    arr.append(root.data)
    preorder(root.left,arr)
    preorder(root.right,arr)
    return arr
def postorder(root,arr):
    if root is None:
        return 
    postorder(root.left,arr)
    postorder(root.right,arr)
    arr.append(root.data)
    return arr 

    
