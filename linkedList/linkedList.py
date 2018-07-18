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

    def isEmpty(self):
        return self.length == 0

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
    def delete(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    # 以索引删除
    def deleteindex(self, index):

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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        node = head
        while (node):
            node = node.next
            count = count + 1

        if count ==1:
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


    def __repr__(self):
        if self.isEmpty():
            print("the chain table is empty")
            return
        nlist = ""
        node = self._head
        while node:
            nlist += node.val
            node = node.next
        return nlist

if __name__ == '__main__':
    chain = LinkedList()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    # F = ListNode('F')
    # G = ListNode('G')

    chain.append(A)
    chain.append(B)
    chain.append(C)
    chain.append(D)
    chain.append(E)
    # chain.append(F)
    # chain.append(G)
   # chain.delete(G)
   #  print(chain)
    chain.removeNthFromEnd(A, 2)
    print(chain)
