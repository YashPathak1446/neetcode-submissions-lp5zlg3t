# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        max_depth = 0
        curr_depth = 0

        def recursive_call(root, curr_depth):
            nonlocal max_depth
            curr_depth += 1
            if root.left:
                recursive_call(root.left, curr_depth)
            if root.right:
                recursive_call(root.right, curr_depth)
            max_depth = max(max_depth, curr_depth)
            
        recursive_call(root, curr_depth)
        return max_depth