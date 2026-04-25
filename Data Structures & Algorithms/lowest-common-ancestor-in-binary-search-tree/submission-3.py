# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_ancestors = []
        q_ancestors = []

        def traverse(root, ancestors, node):
            if root is None:
                return

            ancestors.append(root.val)

            if node.val < root.val:
                traverse(root.left, ancestors, node)
            elif node.val > root.val:
                traverse(root.right, ancestors, node)
            else:
                return

        traverse(root, p_ancestors, p)
        traverse(root, q_ancestors, q)

        lca = None
        i = 0

        while i < len(p_ancestors) and i < len(q_ancestors):
            if p_ancestors[i] == q_ancestors[i]:
                lca = p_ancestors[i]
                i += 1
            else:
                break

        def dfs(root, lca):
            if root.val == lca:
                return root
            elif root.val < lca:
                return dfs(root.right, lca)
            else:
                return dfs(root.left, lca)

        return dfs(root, lca)