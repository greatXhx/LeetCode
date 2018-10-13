class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class LinkedList:
    def __init__(self):
        self._head = None
        self.length = 0

    # 判断是否为空
    def isEmpty(self):
        return self.length == 0

    # 在链表尾部增加节点
    def append(self, item):

        if isinstance(item, ListNode):
            node = item
        else:
            node = ListNode(item)

        if self._head is None:
            self._head = node
        else:
            be_node = self._head
            while be_node.next:
                be_node = be_node.next
            be_node.next = node
        self.length += 1

    # 以节点删除
    def deleteByNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        self.length -= 1

    # 以索引删除
    def deleteByIndex(self, index):

        if self.isEmpty():
            print('this chain table is empty')
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return
        # if index == 0
        #     self._head = None
        else:
            node = self._head
            count = 0
            while True:
                count += 1
                if index == count:
                    node._next = node._next._next
                    break
                node = node._next

        self.length -= 1

    # 删除链表的倒数第 n 个节点，并且返回链表的头结点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        node = head
        while (node):
            node = node.next
            count = count + 1

        if count == 1:
            return None

        node = head
        for i in range(count - n - 1):
            node = node.next

        if n > 1 and n<count:
            node.next.val = node.next.next.val
            node.next.next = node.next.next.next
        elif n == count:
            node.val = node.next.val
            node.next = node.next.next
        elif n == 1:
            node.next = None

        self.length -= 1

        return head

    # 翻转单链表
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

    # 翻转单链表
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

        newHead = self.reverseListRecursion(head.next)
        head.next.next = head
        head.next = None
        self._head = newHead
        return newHead

    def __repr__(self):
        if self.isEmpty():
            print("the chain table is empty")
            return
        nlist = ""
        node = self._head
        while node:
            nlist += str(node.val) + ','
            node = node.next
        return nlist

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        temp1 = l1 if l1.val<l2.val else l2
        temp2 = l2 if l1.val<l2.val else l1

        while temp2:
            if temp1.next is None:
                temp1.next = temp2
                break
            elif temp1.next.val <   temp2.val:
                temp1 = temp1.next
            else:
                temp1Next = temp1.next
                temp2Insert = ListNode(temp2.val)
                temp1.next = temp2Insert
                temp2Insert.next = temp1Next
                temp1 = temp1.next
                temp2 = temp2.next
        return l1 if l1.val < l2.val else l2

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

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False






if __name__ == '__main__':
    s1 = Solution()
    chain1 = LinkedList()
    chain2 = LinkedList()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(2)
    E = ListNode(1)

    chain1.append(A)
    chain1.append(B)
    # chain1.append(C)
    # chain1.append(D)
    # chain1.append(E)

    A1 = ListNode(2)
    B1 = ListNode(4)
    C1 = ListNode(6)
    D1 = ListNode(8)
    E1 = ListNode(10)

    chain2.append(A1)
    chain2.append(B1)
    chain2.append(C1)
    chain2.append(D1)
    chain2.append(E1)

    print(s1.hasCycle(A))