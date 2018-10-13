""""
这道题是要将有序数组转为二叉搜索树，所谓二叉搜索树，是一种始终满足左<根<右（另外一种更直白的解释，二叉搜索树：空树或者二叉树的所有节点比他的左子节点大，比他的右子节点小。）的特性的二叉树，如果将二叉搜索树按中序遍历的话，得到的就是一个有序数组了。那么反过来，我们可以得知，根节点应该是有序数组的中间点，从中间点分开为左右两个有序数组，在分别找出其中间点作为原中间点的左右两个子节点，这不就是二分查找法的核心思想么。所以这道题考的就是二分查找法
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid+1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root

