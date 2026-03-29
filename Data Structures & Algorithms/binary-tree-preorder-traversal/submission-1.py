# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre_order_lst = []
        def recurse(root):
            if root is None:
                return
            pre_order_lst.append(root.val)
            if root.left:
                recurse(root.left)
            if root.right:
                recurse(root.right)
            
        recurse(root)
        return pre_order_lst 
