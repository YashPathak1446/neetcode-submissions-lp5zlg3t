# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    good_nodes = 0
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        max_so_far = root.val

        def dfs(root, max_so_far):
            if root is None:
                return
            
            if root and root.val >= max_so_far:
                self.good_nodes += 1
                max_so_far = root.val
            dfs(root.left, max_so_far)
            dfs(root.right, max_so_far)
        
        dfs(root, max_so_far)
        return self.good_nodes
        