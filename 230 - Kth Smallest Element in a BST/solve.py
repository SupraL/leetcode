# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root):
        if root:
            l = self.traversal(root.left)
            self.stack.append(root.val)
            r = self.traversal(root.right)
        else:
            return None
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.stack = []
        self.traversal(root)
        return self.stack[k-1]