# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        curr_depth = 0
        level_lst = []
        level_dict = {}
        def dfs(root, curr_depth):
            if root is None:
                return
            if curr_depth not in level_dict:
                level_dict[curr_depth] = [root.val]
            else:
                level_dict[curr_depth].append(root.val)

            dfs(root.left, curr_depth + 1)
            dfs(root.right, curr_depth + 1)
        dfs(root, curr_depth)
        for k, v in level_dict.items():
            level_lst.append(v)
        return level_lst
        