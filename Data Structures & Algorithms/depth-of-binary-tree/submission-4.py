# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_depth = 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(root, depth):
            if root is None:
                self.max_depth = 0
                return
                
            if root.left is None and root.right is None:
                self.max_depth = max(self.max_depth, depth)
                return
                
            if root.left:
                traverse(root.left, depth + 1)
            
            if root.right:
                traverse(root.right, depth + 1)
        
        traverse(root, 1)
        return self.max_depth
