# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur_node = head
        pre_node = head
        
        if head == None:
            return None
        
        while head.val == val:
            head = head.next
            if head == None:
                break
            
        while cur_node:
            if cur_node.val == val:
                pre_node.next = cur_node.next
                cur_node = pre_node.next
            else:
                pre_node = cur_node
                cur_node = cur_node.next
        return head