# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev_pointer = None
        while cur:
            next_pointer = cur.next
            cur.next = prev_pointer
            prev_pointer = cur
            cur = next_pointer
        head = prev_pointer
        return head