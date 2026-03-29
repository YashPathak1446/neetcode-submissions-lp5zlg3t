# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        post_order_list = []

        def recursive_call(root):
            if root.left:
                recursive_call(root.left)
            if root.right:
                recursive_call(root.right)
            post_order_list.append(root.val)

        recursive_call(root)
        
        return post_order_list