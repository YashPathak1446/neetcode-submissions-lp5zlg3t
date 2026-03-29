# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0

        depth = 0
        depth2 = 0

        if (root.left != None):
            depth = 1 + self.maxDepth(root.left)
        if (root.right != None):
            depth2 = 1 + self.maxDepth(root.right)
        # if both left and right are null
        if (root.left == None and root.right == None):
            return 1
        
        return max(1, depth, depth2)