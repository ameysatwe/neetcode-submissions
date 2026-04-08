# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        vals = []
        # nodes = ListNode()
        curr = head
        while head:
            vals.append(head)
            head = head.next
        
        # print(vals)
        i,j = 0,len(vals)-1

        while i < j:
            vals[i].next = vals[j]
            i+=1
            if i>=j:
                break
            vals[j].next = vals[i]
            j-=1
        
        vals[i].next = None
