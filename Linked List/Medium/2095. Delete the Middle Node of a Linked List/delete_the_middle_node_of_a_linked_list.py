# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None  

        prev_slow = None
        slow = head
        fast = head

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev_slow.next = slow.next
        del slow 
        return head
