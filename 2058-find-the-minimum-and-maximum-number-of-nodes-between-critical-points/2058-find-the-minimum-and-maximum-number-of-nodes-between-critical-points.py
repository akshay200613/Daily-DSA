# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        idx = 1                     
        prev = head
        curr = head.next
        cp_indices = []

        while curr.next:
            idx += 1               
            nxt = curr.next

            if (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val):
                cp_indices.append(idx)

            prev = curr
            curr = nxt

        if len(cp_indices) < 2:
            return [-1, -1]

        
        max_dist = cp_indices[-1] - cp_indices[0]

        
        min_dist = float('inf')
        for i in range(1, len(cp_indices)):
            min_dist = min(min_dist, cp_indices[i] - cp_indices[i - 1])

        return [min_dist, max_dist]
        