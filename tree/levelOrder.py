from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack = [root]
        output = []
        while stack:
            output1 = []
            for i in range(len(stack)):
                current = stack.pop(0)
                output1.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            output.append(output1)
        return output

    def levelOrder1(self, root):
        if root is None:
            return []
        q = deque([root])
        output = []

        while q:
            output1 = []
            for i in range(len(q)):
                current = q.popleft()
                output1.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            output.append(output1)
        return output


