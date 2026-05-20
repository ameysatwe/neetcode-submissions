# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrap:
    def __init__(self,node):
        self.node = node
    
    def __lt__(self,other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        curr = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap,NodeWrap(lst))

        while minHeap:
            node_w = heapq.heappop(minHeap)
            curr.next = node_w.node
            curr = curr.next

            if node_w.node.next:
                heapq.heappush(minHeap,NodeWrap(node_w.node.next))
        
        return res.next