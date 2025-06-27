#(Time : O(n), Space : O(1))

#Approach-1 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_start = even

        while even and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_start
        return head

#Approach-2
if not head or not head.next or not head.next.next:
            return head

        # Count number of nodes
        start = head
        end = head
        count = 1
        while end.next:
            end = end.next
            count += 1

        count //= 2  # Number of even-position nodes

        while count:
            start_next = start.next
            start.next = start_next.next  # skip one node

            end.next = start_next
            start = start.next
            end = end.next
            count -= 1

        end.next = None
        return head
