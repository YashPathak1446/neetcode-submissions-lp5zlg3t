# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max_d = 0


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root):
            # First, find the height for the leaf nodes. This is the base case.
            # The height is always 0 for any leaf.
            if root is None:
                return 0
            height_left = traverse(root.left)
            height_right = traverse(root.right)

            self.max_d = max(self.max_d, height_left + height_right)

            return 1 + max(height_left, height_right)

        traverse(root)
        return self.max_d