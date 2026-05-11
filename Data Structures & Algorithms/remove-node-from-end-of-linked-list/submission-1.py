# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rec(self,head,n):
        if not head:
            return None

        head.next = self.removeNthFromEnd(head.next,n)
        # n[0] -=1
        self.x-=1
        if self.x == 0:
            return head.next
        return head



    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        self.x = n
        return self.rec(head,n)

    