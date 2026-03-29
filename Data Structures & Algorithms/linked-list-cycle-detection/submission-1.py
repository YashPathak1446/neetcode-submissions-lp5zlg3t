# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp1 = head
        set_list_nodes = set()
        while temp1:
            if temp1 in set_list_nodes:
                return True
            set_list_nodes.add(temp1)
            temp1 = temp1.next
        return False
