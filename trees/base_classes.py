class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        """
        Create new tree node
        :param key: the component on which the nodes is ordered within a tree {any}
        :param val: the value associated with the key {any}
        :param left: left sub-node {TreeNode}
        :param right: right sub-node {TreeNode}
        :param parent: parent node {TreeNode}
        """
        self.key = key
        self.payload = val
        for node in [left, right, parent]:
            if node and not isinstance(node, TreeNode):
                raise TypeError("Only TreeNode class is valid")
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        """
        True if has left child, false otherwise
        :return: bool
        """
        return self.leftChild

    def hasRightChild(self):
        """
        True if has right child, false otherwise
        :return: bool
        """
        return self.rightChild

    def isLeftChild(self):
        """
        True if is left child, false otherwise
        :return: bool
        """
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        """
        True if is right child, false otherwise
        :return: bool
        """
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        """
        True if is root, false otherwise
        :return: bool
        """
        return not self.parent

    def isLeaf(self):
        """
        True if is leaf, false otherwise
        :return: bool
        """
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """
        True if has any children, false otherwise
        :return: bool
        """
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """
        True if has both children, false otherwise
        :return: bool
        """
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinaryTree(object):
    """
    Base binary tree object
    """
    def __init__(self, key):
        """
        Create new binary tree object
        :param key: value contained by the node {any}
        """
        self.key = key
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, key):
        """
        Insert node as left child of root
        :param key: value contained by the node {any}
        :return: none
        """
        if self.leftChild is None:
            self.leftChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,key):
        """
        Insert node as right child of root
        :param key: value contained by the node {any}
        :return: none
        """
        if self.rightChild is None:
            self.rightChild = BinaryTree(key)
        else:
            t = BinaryTree(key)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        """
        Get the right child tree of the present node
        :return: BinaryTree
        """
        return self.rightChild

    def getLeftChild(self):
        """
        Get the left child tree of the present node
        :return: BinaryTree
        """
        return self.leftChild

    def setRootVal(self, key):
        """
        Replace the key of the root node
        :param key: {any}
        :return: none
        """
        self.key = key

    def getRootVal(self):
        """
        Return the key of the root node
        :return: {any}
        """
        return self.key