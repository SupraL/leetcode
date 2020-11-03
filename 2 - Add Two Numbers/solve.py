# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def node_to_str(self, l):
        out = ""
        while l != None:
            out += str(l.val)
            l = l.next
        return out
    
    def str_to_node(self, s):
        if len(s) > 0:
            n = ListNode(int(s[0]))
            dummy_node = n
            for i in range(1, len(s)):
                dummy_node.next = ListNode(s[i])
                dummy_node = dummy_node.next
            return n
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = int(self.node_to_str(l1)[::-1])
        l2_num = int(self.node_to_str(l2)[::-1])
        ans = l1_num + l2_num
        return self.str_to_node(str(ans)[::-1])