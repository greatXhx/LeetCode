class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Tree:
    """树类"""
    def __init__(self):
        self.root = None
        # self.myQueue = []

    def add(self, x):
        node = TreeNode(x)
        if self.root is None:
            self.root = node
            # self.myQueue.append(self.root)
        else:
            q = [self.root]
            while True:
                popNode = q.pop(0)
                if popNode.left is None:
                    popNode.left = node
                    return
                elif popNode.right is None:
                    popNode.right = node
                    return
                else:
                    q.append(popNode.left)
                    q.append(popNode.right)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            depthL = 1
            depthR = 1
        else:
            return 0

        depthL += self.maxDepth(root.left)
        depthR += self.maxDepth(root.right)

        return depthL if depthL>depthR else depthR

    def validBST(self, root, small, large):
        if root == None:
            return True
        if small <= root.val or large>= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, -2**32,2**32-1)

    


if __name__ =="__main__":
    root = TreeNode("root")
    T2 = TreeNode(2)
    tree = Tree()  # 新建一个树对象
    tree.add(root)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    # print(tree.maxDepth(tree.root))
    print(tree.isValidBST(tree.root))