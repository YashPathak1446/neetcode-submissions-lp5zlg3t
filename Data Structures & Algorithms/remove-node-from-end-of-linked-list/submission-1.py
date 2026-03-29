# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        count = 0
        index_to_remove = length - n
        if index_to_remove == 0:
            return head.next
        temp2 = head
        while temp2:
            
            if count+1 == index_to_remove:
                temp2.next = temp2.next.next

            temp2 = temp2.next
            count += 1
        
        return head
        