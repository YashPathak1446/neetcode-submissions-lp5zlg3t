# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Step 1: find mid of list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # beginning of second half of list is currently slow.next
        second = slow.next
        # split the list
        slow.next = None
        
        # now reverse the second half of the list
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # finally merge the two lists, set first to head and second to prev (which is new head of reversed list)
        first = head
        second = prev
        # Second is shorter
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
    