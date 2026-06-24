# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        curr = head

        while curr:
            l += 1
            curr = curr.next
        curr = head
        r = 1
        if l - n == 0:
            return head.next
        while curr:
            if r == (l - n):
                curr.next = curr.next.next
            else:
                curr = curr.next
            r += 1
        return head
            