# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    in_order_traversal = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left then root then right
        if root == None:
            return []
        in_order_traversal = []
        def recurse_function(root):
            if root.left:
                recurse_function(root.left)
            in_order_traversal.append(root.val)
            if root.right:
                recurse_function(root.right)
        recurse_function(root)
        
        return in_order_traversal