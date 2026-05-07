# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     left = self.height(root.left)
    #     right = self.height(root.right)

    #     if abs(left-right)>1:
    #         return False

    #     return self.isBalanced(root.left) and self.isBalanced(root.right)    

    # def height(self,node):
    #     if not node:
    #         return 0
        
    #     return 1+max(self.height(node.left),self.height(node.right))

        def dfs(node):
            if not node:
                return [True,0]
            
            l,r = dfs(node.left),dfs(node.right)
            balanced = l[0] and r[0] and abs(l[1]-r[1])<=1

            return [balanced,1+max(l[1],r[1])]
        
        return dfs(root)[0]