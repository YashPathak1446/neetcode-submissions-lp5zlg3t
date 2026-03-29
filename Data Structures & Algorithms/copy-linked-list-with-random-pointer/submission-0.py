"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # base case is where the Node is None,
        # The copy must also map to None
        old_to_copy = {None:None}
        
        temp = head
        # Map the original to the copy list; create new nodes for copy
        # These all exist as copy nodes (separate with same val) but not linked
        while temp:
            copy = Node(temp.val)
            old_to_copy[temp] = copy
            temp = temp.next
        
        temp = head
        # Now loop and do the pointer matching
        while temp:
            # access the copy
            copy = old_to_copy[temp]
            # map copy next to the copy of the next temp node
            copy.next = old_to_copy[temp.next]
            # map copy random to the copy of the random temp node
            copy.random = old_to_copy[temp.random]
            temp = temp.next
        
        # Return the head of the copy node through the dict
        return old_to_copy[head]

