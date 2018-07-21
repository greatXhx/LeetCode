# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if root:
        #     depthL = 1
        #     depthR = 1
        # else:
        #     return 0
        #
        # depthL += self.maxDepth(root.left)
        # depthR += self.maxDepth(root.right)
        #
        # return depthL if depthL>depthR else depthR

        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))