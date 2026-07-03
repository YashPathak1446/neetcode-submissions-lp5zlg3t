"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # x = node.neighbors[0].neighbors[1] # 3
        # print(x.val)
        if node == None:
            return
        
        return_lst = []
        original_to_clone = dict()
        def dfs(curr_node):
            if curr_node in original_to_clone:
                return original_to_clone[curr_node]
            new_node = Node(val = curr_node.val)
            original_to_clone[curr_node] = new_node
            neighbors = []
            for i in range(len(curr_node.neighbors)):
                clone = dfs(curr_node.neighbors[i])
                if clone is not None:
                    neighbors.append(clone)
            new_node.neighbors = neighbors
            return new_node
        clone = dfs(node)
        return clone
