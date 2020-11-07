# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = head
        pervious_node = head
        
        #Version2
        while dummy_node is not None:
            if dummy_node.next == None:
                break
            if dummy_node.val == dummy_node.next.val:
                dummy_node.next = dummy_node.next.next
            else:
                dummy_node = dummy_node.next
        
        #Version 1
        """while dummy_node is not None:
            if dummy_node.val not in lst:
                lst[dummy_node.val] = 1
                pervious_node = dummy_node
                dummy_node = dummy_node.next
            else:
                pervious_node.next = dummy_node.next
                dummy_node = pervious_node.next"""
        return head