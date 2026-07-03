"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return

        original_to_clone = dict()

        def dfs(curr_node):
            if curr_node in original_to_clone:
                return original_to_clone[curr_node]
                
            new_node = Node(val = curr_node.val)
            original_to_clone[curr_node] = new_node

            for neighbor in curr_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))

            return new_node

        clone = dfs(node)
        return clone
