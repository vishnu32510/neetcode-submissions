# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Fast and Slow Pointer
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

        # HashSet
        # seen = set()

        # curr = head

        # while curr:
        #     if curr in seen:
        #         return True
        #     seen.add(curr)
        #     curr = curr.next
        # return False