# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head, left, right):

        # If list has one node or nothing to reverse
        if not head or left == right:
            return head

        # Dummy node helps when left = 1
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node just before 'left'
        for i in range(left - 1):
            prev = prev.next

        # curr is the first node of the part to reverse
        curr = prev.next

        # Reverse the nodes
        for i in range(right - left):
            nxt = curr.next          # Save next node
            curr.next = nxt.next     # Remove nxt from its position
            nxt.next = prev.next     # Insert nxt at front of reversed part
            prev.next = nxt

        return dummy.next