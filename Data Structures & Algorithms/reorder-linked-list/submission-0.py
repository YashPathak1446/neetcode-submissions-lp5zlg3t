# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        prev = None
        arr = []
        length = 0

        # while temp:
        #     arr.append(temp.val)
        #     right = temp.next
        #     temp.next = prev
        #     prev = temp
        #     temp = right
        #     length += 1
        # while prev:
        #     print(prev.val)
        #     prev = prev.next
        while temp:
            arr.append(temp.val)
            temp = temp.next

        i = 0
        while i < len(arr):
            if i%2 == 0:
                i += 1
            else:
                end = arr.pop()
                arr.insert(i, end)
                i += 1
        print(arr)
        i = 0
        while head:
            head.val = arr[i]
            i += 1
            head = head.next
