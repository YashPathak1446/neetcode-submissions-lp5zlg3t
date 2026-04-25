# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_valid = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, min_so_far, max_so_far):
            if root is None:
                return
            
            if not min_so_far < root.val < max_so_far:
                self.is_valid = False
                return
            
            dfs(root.left, min_so_far, root.val)
            dfs(root.right, root.val, max_so_far)
            

        dfs(root, float('-inf'), float('inf'))
        return self.is_valid