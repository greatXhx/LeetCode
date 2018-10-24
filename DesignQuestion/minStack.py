class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min == None or self.min>x:
            self.min = x

    def pop(self):
        """
        :rtype: void
        """
        popItem = self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
            return popItem
        if popItem == self.min:
            self.min = self.stack[0]
            for i in self.stack:
                if self.min > i:
                    self.min = i
        return popItem

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()