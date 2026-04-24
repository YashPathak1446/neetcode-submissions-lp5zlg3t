# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if root is None:
                return 0
            height_left = traverse(root.left)
            height_right = traverse(root.right)

            if abs(height_left - height_right) > 1:
                self.is_balanced = False
            
            return 1 + max(height_left, height_right)
        traverse(root)
        return self.is_balanced