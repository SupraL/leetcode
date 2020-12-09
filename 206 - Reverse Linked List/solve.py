# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pervious = None
        cur_node = head
        while cur_node != None:
            tmp = cur_node.next
            cur_node.next = pervious
            pervious = cur_node
            cur_node = tmp
        return pervious