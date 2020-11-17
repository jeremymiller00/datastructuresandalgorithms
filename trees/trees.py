'''
Implementations of standard tree data structure
'''

class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
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

class BinaryHeap:
    '''
    Binary heap data structure

    From https://en.wikipedia.org/wiki/Binary_heap#:~:text=A%20binary%20heap%20is%20a,a%20data%20structure%20for%20heapsort.
    A binary heap is defined as a binary tree with two additional constraints:[3]

    Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
    Heap property: the key stored in each node is either greater than or equal to (≥) or less than or equal to (≤) the keys in the node's children, according to some total order.
    '''
    def __init__(self):
        '''
        a binary heap represented as a Python list
        '''
        self.heapList = [0]
        self.currentSize = 0

    def _percUp(self, i):
        '''
        move item up the heap to maintain heap property
        '''
        while i // 2 > 0:
            if self.heaplist[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        '''
        adds new item to the heap
        '''
        self.heapList.append(k)
        self.currentSize += 1
        self._percUp(self.currentSize)

    def findMin(self):
        '''
        returns item with min key value, leaving item in the heap
        '''
        return self.heapList[1]

    def _percDown(self, i):
        '''
        swap root with smallest child that is less than the root
        continue until root is less that both its children
        '''
        while (i * 2) < self.currentSize:
            mc = self._minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def _minChild(self, i):
        '''
        return the index of the smaller of two child nodes
        '''
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < if self.heapList[i * 2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        '''
        returns item with min key value, removing item from the heap
        remove first item
        move last item to first position, maintains heap structure property
        percolate down the first item, restores heap order property
        '''
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self._percDown(1)
        return retval

    def minChild(self, i):
        # check if node has two children, if not return first child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
            return i * 2
        return i * 2 + 1

    def isEmpty() -> bool:

    def size() -> int:
        '''
        returns the number of items in the heap
        '''

    def buildHeap(self, lst):
        '''
        builds a new heap from a list of keys
        '''
        i = len(lst) // 2
        self.currentSize = len(lst)
        self.heapList = [0] + lst[:]
        while i > 0:
            self.percDown(i)
            i -= 1