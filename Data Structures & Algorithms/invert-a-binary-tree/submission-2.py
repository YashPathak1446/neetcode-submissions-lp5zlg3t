# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root):
            if root is None:
                return
            if root.left:
                recurse(root.left)
            if root.right:
                recurse(root.right)
            temp = root.right
            root.right = root.left
            root.left = temp
        recurse(root)

        return root