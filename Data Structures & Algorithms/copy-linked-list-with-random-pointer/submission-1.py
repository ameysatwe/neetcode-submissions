"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # dummy = Node(-1)
        # mp = {}
        # curr = dummy

        # while head and head.next:
        #     curr = head
        #     mp[head.val] = head.random
        #     curr = curr.next
        
        # print(head)
        # return dummy.next

        mp = {}

        if not head:
            return None

        curr = head

        while curr:
            mp[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            mp[curr].next = mp.get(curr.next)
            mp[curr].random = mp.get(curr.random)
            curr = curr.next
        
        return mp[head]
