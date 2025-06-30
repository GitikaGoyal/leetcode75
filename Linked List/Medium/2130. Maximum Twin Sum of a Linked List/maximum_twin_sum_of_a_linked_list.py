#Approach-1 (Using vector/array)
#T.C.->O(n)
#S.C.->O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        
        # Step 1: Traverse the list and store values
        while head:
            values.append(head.val)
            head = head.next
        
        # Step 2: Compute maximum twin sum
        i, j = 0, len(values) - 1
        max_sum = 0

        while i < j:
            max_sum = max(max_sum, values[i] + values[j])
            i += 1
            j -= 1

        return max_sum
        
#Approach-2 (Using Stack)
#T.C.->O(n)
#S.C.->O(n) for stack
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        
        # Step 1: Push all node values onto the stack
        while curr:
            stack.append(curr.val)
            curr = curr.next
        
        # Step 2: Pop values from the stack while traversing the first half
        curr = head
        result = 0
        n = len(stack)
        count = 1
        
        while count <= n // 2:
            result = max(result, curr.val + stack.pop())
            curr = curr.next
            count += 1
        
        return result

        


#Approach-3 (Reversing the second half of the linkedlist)
#T.C.->O(n)
#S.C.->O(1)
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Calculate max twin sum
        result = 0
        first = head
        second = prev
        while second:
            result = max(result, first.val + second.val)
            first = first.next
            second = second.next
        
        return result
