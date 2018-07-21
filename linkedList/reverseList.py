class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        lastTemp = None
        while temp:
            nextTemp = temp.next
            temp.next = lastTemp
            lastTemp = temp
            temp = nextTemp
        self._head = lastTemp
        return lastTemp


    def reverseListRecursion(self, head):
        "递归解法"
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return
        if head.next is None:
            return head

        newHead = Solution.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        return newHead