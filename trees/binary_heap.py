class BinaryHeap:
    """
    Binary heap data structure

    From https://en.wikipedia.org/wiki/Binary_heap#:~:text=A%20binary%20heap%20is%20a,a%20data%20structure%20for%20heapsort.
    A binary heap is defined as a binary tree with two additional constraints:[3]

    Shape property: a binary heap is a complete binary tree; that is, all levels of the tree, except possibly the last one (deepest) are fully filled, and, if the last level of the tree is not complete, the nodes of that level are filled from left to right.
    Heap property: the key stored in each node is either greater than or equal to (≥) or less than or equal to (≤) the keys in the node's children, according to some total order.
    """
    def __init__(self):
        """
        A binary heap represented via a Python list
        Adding an initial "0" value makes perc operations more simple
        """
        self.heap_list = [0]
        self.current_size = 0

    def _perc_up(self, i):
        """
        move item up the heap to maintain heap property
        """
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self, k):
        """
        adds new item to the heap
        """
        self.heap_list.append(k)
        self.current_size += 1
        self._perc_up(self.current_size)

    def find_min(self):
        """
        returns item with min key value, leaving item in the heap
        """
        return self.heap_list[1]

    def _perc_down(self, i):
        """
        swap root with smallest child that is less than the root
        continue until root is less than both its children
        """
        while (i * 2) <= self.current_size:
            mc = self._min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def _min_child(self, i):
        """
        return the index of the smaller of two child nodes
        """
        if i * 2 + 1 > self.current_size:
            return i * 2
        elif self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_min(self):
        """
        returns item with min key value, removing item from the heap
        remove first item
        move last item to first position, maintains heap structure property
        percolate down the first item, restores heap order property
        """
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self._perc_down(1)
        return retval

    def is_empty(self) -> bool:
        """
        Returns True if heap empty, False otherwise
        :return: bool
        """
        return self.current_size == 0

    def size(self) -> int:
        """
        returns the number of items in the heap
        """
        return self.current_size

    def build_heap(self, lst):
        """
        builds a new heap from a list of keys
        """
        i = len(lst) // 2
        self.current_size = len(lst)
        self.heap_list = [0] + lst[:]
        while i > 0:
            self._perc_down(i)
            i -= 1