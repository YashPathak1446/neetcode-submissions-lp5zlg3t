# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        num1 = ""
        num2 = ""
        while temp1:
            num1 += str(temp1.val)
            temp1 = temp1.next
        while temp2:
            num2 += str(temp2.val)
            temp2 = temp2.next
        
        num1 = int(num1[::-1])
        num2 = int(num2[::-1])
        sum_nums = str(num1 + num2)[::-1]
        sum_list = temp = ListNode()
        count = 0

        for i in range(len(sum_nums)):
            temp.val = int(sum_nums[i])
            count += 1
            if count == len(sum_nums):
                break
            temp.next = ListNode()
            temp = temp.next
        
        return sum_list