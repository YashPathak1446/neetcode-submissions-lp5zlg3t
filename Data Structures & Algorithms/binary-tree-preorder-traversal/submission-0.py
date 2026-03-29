# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        pre_order_traversal_list = []

        def recursive_call(root):
            pre_order_traversal_list.append(root.val)
            if root.left:
                recursive_call(root.left)
            if root.right:
                recursive_call(root.right)
        
        recursive_call(root)
        return pre_order_traversal_list
            