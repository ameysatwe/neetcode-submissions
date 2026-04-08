# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # msf = -1
        # cnt = 0
        def dfs(node,msf):
            # nonlocal cnt
            if not node:
                return 0
            
            res = 1 if node.val>=msf else 0

            msf = max(msf,node.val)

            res += dfs(node.left,msf)
            res += dfs(node.right,msf)

            return res
        

        return dfs(root,root.val)
            



