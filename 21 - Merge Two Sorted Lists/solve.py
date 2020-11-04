# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_ptr = l1
        l2_ptr = l2

        result_node = ListNode(0)
        dummy_node = result_node

        while l1_ptr is not None or l2_ptr is not None:
            if l1_ptr == None:
                dummy_node.next = ListNode(l2_ptr.val)
                l2_ptr = l2_ptr.next
                dummy_node = dummy_node.next
                continue

            if l2_ptr == None:
                dummy_node.next = ListNode(l1_ptr.val)
                l1_ptr = l1_ptr.next
                dummy_node = dummy_node.next
                continue
                
            if l1_ptr.val > l2_ptr.val:
                dummy_node.next = ListNode(l2_ptr.val)
                l2_ptr = l2_ptr.next
            else:
                dummy_node.next = ListNode(l1_ptr.val)
                l1_ptr = l1_ptr.next
            dummy_node = dummy_node.next
        return result_node.next