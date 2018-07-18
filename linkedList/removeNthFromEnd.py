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

    # 链表长度为1 ，直接删
    if count == 1:
        return None

    node = head
    for i in range(count - n - 1):     #多减1是为了能删尾节点
        node = node.next

    if n > 1 and n < count:              #删中间节点
        node.next.val = node.next.next.val
        node.next.next = node.next.next.next
    elif n == count:                     #删头结点
        node.val = node.next.val
        node.next = node.next.next
    elif n == 1:                         #删尾节点
        node.next = None

def removeNthFromEndBestSummit(self, head, n):
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