# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfsPreorder(root1,root2):
            if root1 == None and root2 == None:
                return
            elif root1 == None:
                return root2
            elif root2 == None:
                return root1
            else:
                root = TreeNode(root1.val + root2.val)     
                root.left = dfsPreorder(root1.left, root2.left)
                root.right = dfsPreorder(root1.right, root2.right)      
            return root
        
        return dfsPreorder(root1, root2)