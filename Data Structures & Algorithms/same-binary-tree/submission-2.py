# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    same_tree = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(p, q):
            if p is None or q is None:
                if p is None and q is not None:
                    self.same_tree = False
                    return
                elif p is not None and q is None:
                    self.same_tree = False
                    return
                else:
                    return
            elif p.val == q.val:
                traverse(p.left, q.left)
                traverse(p.right, q.right)
            else:
                self.same_tree = False
        
        traverse(p, q)
        return self.same_tree