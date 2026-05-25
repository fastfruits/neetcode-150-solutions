# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrevious = dummy

        while True:
            kth = self.getKth(groupPrevious, k)
            if not kth: 
                break

            groupNext = kth.next

            prev = kth.next
            curr = groupPrevious.next
            #Reverse k nodes
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            #Connect to main
            temp = groupPrevious.next #Old head of group
            groupPrevious.next = kth #Connect to kth node
            temp.next = groupNext #Connect old head to list
            groupPrevious = temp #Move groupPrevious to tail of reversed

        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr