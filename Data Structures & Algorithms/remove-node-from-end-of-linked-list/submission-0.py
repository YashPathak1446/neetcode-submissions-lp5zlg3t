# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length_list = 0
        while temp!= None:
            length_list += 1
            temp = temp.next
        print(length_list)
        node_to_remove = length_list - n
        temp = head
        curr_count = 0
        if length_list == 1:
            return None
        if node_to_remove == 0:
            return head.next
        while curr_count != node_to_remove - 1:
            temp = temp.next
            curr_count += 1
        temp.next = temp.next.next
        return head
        