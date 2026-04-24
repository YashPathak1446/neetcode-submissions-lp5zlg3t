# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        in_order_lst = []
        
        def traverse(root):
            if root is None:
                return
            if root.left:
                traverse(root.left)
            in_order_lst.append(root.val)
            if root.right:
                traverse(root.right)
        
        traverse(root)
        return in_order_lst