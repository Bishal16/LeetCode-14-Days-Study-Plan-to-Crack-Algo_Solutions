# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        c=0
        while node:
            c+=1
            node = node.next
        i=1
        c=c//2+1
        node = head
        while i<c:
            node = node.next
            i+=1
        return node
# appr -2:     When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. When fast reaches the end of the list, slow must be in the middle.