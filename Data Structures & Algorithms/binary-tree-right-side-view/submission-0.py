# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        right_lst = []
        level_set = set()

        def dfs(root, curr_level):
            if root is None:
                return
            if curr_level not in level_set:
                right_lst.append(root.val)
                level_set.add(curr_level)
            dfs(root.right, curr_level + 1)
            dfs(root.left, curr_level + 1)
        
        dfs(root, 0)
        return right_lst