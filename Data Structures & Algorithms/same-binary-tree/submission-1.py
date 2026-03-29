# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            if q is not None:
                return False
            return True
        if q is None:
            if p is not None:
                return False
            return True
        
        self.output = True
        def recurse(p, q):
            if p.val != q.val:
                self.output = False
                return
            
            if p.left and q.left:
                recurse(p.left, q.left)
            else:
                if p.left != q.left:
                    self.output = False
                    return
                
            if p.right and q.right:
                recurse(p.right, q.right)
            else:
                if p.right != q.right:
                    self.output = False
                    return
            
        
        recurse(p, q)
        return self.output