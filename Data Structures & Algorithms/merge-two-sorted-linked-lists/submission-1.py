# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # [(0)->(1, null)]
        output_list = ListNode() # node with val=0, next=None
        head = output_list # head of output_list

        while (list1 and list2):
            if list1.val < list2.val:
                output_list.next = ListNode(val = list1.val)
                list1 = list1.next
                output_list = output_list.next
            
            else:
                output_list.next = ListNode(val = list2.val)
                list2 = list2.next
                output_list = output_list.next
            
        while (list1):
            output_list.next = ListNode(val = list1.val)
            list1 = list1.next
            output_list = output_list.next
        
        while (list2):
            output_list.next = ListNode(val = list2.val)
            list2 = list2.next
            output_list = output_list.next
        
        return head.next

