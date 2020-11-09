# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root):
        if root:
            r = self.traversal(root.right)
            l = self.traversal(root.left)
            self.sum_count += abs(r - l)
            return r + l + root.val
        else:
            return 0
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum_count = 0
        self.traversal(root)
        return self.sum_count
        
        
        