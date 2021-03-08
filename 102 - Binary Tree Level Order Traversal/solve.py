# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root, level):
        if root:
            if level not in self.tree_dict:
                self.tree_dict[level] = []
            self.tree_dict[level].append(root.val)
            self.traversal(root.left, level + 1)
            self.traversal(root.right, level + 1)
        else:
            return None
        
        
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.tree_dict = {}
        self.traversal(root, 0)
        return self.tree_dict.values()