# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        length = 0
        cursor =nextCursor = head
        lastCursor = None
        while cursor:
            cursor = cursor.next
            length += 1

        cursor = head
        for i in range(int(length/2)):
            nextCursor = cursor.next
            cursor.next = lastCursor
            lastCursor = cursor
            cursor = nextCursor

        if length % 2:
            cursor = cursor.next

        while cursor and lastCursor:
            if cursor.val != lastCursor.val:
                return False
            cursor = cursor.next
            lastCursor = lastCursor.next

        return True