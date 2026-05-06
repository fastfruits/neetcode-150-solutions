# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        
        while current:
            next = current.next #get next node
            current.next = previous #reverse the next one to previous

            previous = current
            current = next
        
        return previous


