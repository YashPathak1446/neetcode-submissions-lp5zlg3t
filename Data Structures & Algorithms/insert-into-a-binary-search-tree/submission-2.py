# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            return TreeNode(val)

        def dfs(root, prevNode, val):
            if root is None:
                if prevNode.val > val:
                    prevNode.left = TreeNode(val)
                else:
                    prevNode.right = TreeNode(val)
                return
            
            if root.val < val:
                dfs(root.right, root, val)
            else:
                dfs(root.left, root, val)
        dfs(root, root, val)
        return root