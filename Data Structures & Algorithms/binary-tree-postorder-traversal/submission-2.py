# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        post_order_lst = []

        def traverse(root):
            if root is None:
                return
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            
            post_order_lst.append(root.val)
    
        traverse(root)
        return post_order_lst