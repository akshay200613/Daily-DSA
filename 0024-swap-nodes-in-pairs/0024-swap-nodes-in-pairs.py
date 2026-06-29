# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: 0 or 1 node → nothing to swap
        if head is None or head.next is None:
            return head

        first = head               # node 1
        second = head.next         # node 2

        # Recursively swap from node 3 onward
        first.next = self.swapPairs(second.next)

        # Put second before first
        second.next = first

        # New head of this segment is 'second'
        return second
        