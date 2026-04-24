# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    is_subtree = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def is_same(root, subRoot):
            if root is None or subRoot is None:
                if root is None and subRoot is not None:
                    return False
                elif root is not None and subRoot is None:
                    return False
                else:
                    # self.is_subtree = True
                    return True
            else:
                if root.val == subRoot.val:
                    left = is_same(root.left, subRoot.left)
                    right = is_same(root.right, subRoot.right)
                    if left == True and right == True:
                        return True
                    else:
                        return False
                else:
                    return False

        def traverse(root, subRoot):
            if root is None:
                return
            if root.val == subRoot.val:
                if is_same(root, subRoot):
                    self.is_subtree = True
                    return
            traverse(root.left, subRoot)
            traverse(root.right, subRoot)
        
        traverse(root, subRoot)
        return self.is_subtree