# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        queue = deque([root])


        while queue:

            level_size = len(queue)
            rs = None

            for _ in range(level_size):
                node = queue.popleft()

                if node:
                    rs = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rs:
                res.append(rs.val)
        
        return res
