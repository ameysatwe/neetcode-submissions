# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def v(n,l,r):
            if not n:
                return True
            
            if not (l<n.val<r):
                return False
            
            return v(n.left,l,n.val) and v(n.right,n.val,r)
        
        return v(root,float('-inf'),float('inf'))