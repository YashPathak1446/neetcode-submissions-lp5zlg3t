# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        
        def recursive_call(root):
            if root.left:
                recursive_call(root.left)
            if root.right:
                recursive_call(root.right)
            # invert
            temp = root.left
            root.left = root.right
            root.right = temp
        
        recursive_call(root)
        
        return root