# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_list_nodes = set()
        while head:
            if head in set_list_nodes:
                return True
            set_list_nodes.add(head)
            head = head.next
        return False
