# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return root

        def dfs(root):
            if root is None:
                return
            
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            if root.left and root.left.val == target and root.left.left == None and root.left.right == None:
                root.left = None
            if root.right and root.right.val == target and root.right.left == None and root.right.right == None:
                root.right = None
            return root
        dfs(root)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root