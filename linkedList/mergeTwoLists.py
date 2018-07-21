class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

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
            elif temp1.next.val < temp2.val:
                temp1 = temp1.next
            else:
                temp1Next = temp1.next
                temp2Insert = ListNode(temp2.val)
                temp1.next = temp2Insert
                temp2Insert.next = temp1Next
                temp1 = temp1.next
                temp2 = temp2.next
        return l1 if l1.val < l2.val else l2