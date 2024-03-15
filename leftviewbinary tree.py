7. left view of binary tree
-------------------------------------------------------------------------------------------------------
def leftview(root,arr,level):
    if root is None:
        return 
    if level==len(arr) and root:
        arr.append(root.data)
    leftview(root.left,arr,level+1)
    leftview(root.right,arr,level+1)
def LeftView(root):
    arr=[]
    if root is None:
        return arr
    level=0
    leftview(root,arr,level)
    return arr
