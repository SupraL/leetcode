# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def node_to_string(self, n):
        output = ""
        while n is not None:
            output += str(n.val)
            n = n.next
        return output
        
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        return int(self.node_to_string(head), 2)