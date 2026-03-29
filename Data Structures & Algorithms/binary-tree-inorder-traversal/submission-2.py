# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_order_lst = []
        def recurse(root):
            if root is None:
                return
            if root.left != None:
                recurse(root.left)
            in_order_lst.append(root.val)
            if root.right != None:
                recurse(root.right)
            
        recurse(root)
        return in_order_lst