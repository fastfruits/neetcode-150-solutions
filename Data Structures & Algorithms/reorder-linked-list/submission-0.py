# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #First find the middle 
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Second reverse the back half
        secondHalf = slow.next
        slow.next = None
        prev = None

        while secondHalf:
            nxt = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nxt
        
        #Lastly merge both halfs interlocking
        first = head
        secondHalf = prev

        while secondHalf:
            temp1 = first.next
            temp2 = secondHalf.next
            first.next = secondHalf
            secondHalf.next = temp1
            first = temp1
            secondHalf = temp2