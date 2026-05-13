# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        placeholder = ListNode(0, head)
        slow = placeholder
        fast = head

        #Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        #Move until fast reaches end
        while fast:
            slow = slow.next
            fast = fast.next

        #Remove nth node from end
        slow.next = slow.next.next

        return placeholder.next
        