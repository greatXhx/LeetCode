# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def recursiveTree(self, left, right):
    if left is None and right is None:
        return True
    elif left is None or right is None:
        return False
    elif left.val == right.val:
        return self.recursiveTree(left.left, right.right) and self.recursiveTree(left.right, right.left)
    else:
        return False


def isSymmetric(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    else:
        return self.recursiveTree(root.left, root.right)

