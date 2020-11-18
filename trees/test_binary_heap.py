from unittest import TestCase
from binary_heap import BinaryHeap

class TestBinaryHeap(TestCase):
    def test_insert(self):
        bh = BinaryHeap()
        bh.insert(10)
        self.assertEqual(bh.heap_list[1], 10)
        bh.insert(30)
        self.assertEqual(bh.heap_list[2], 30)
        bh.insert(40)
        self.assertEqual(bh.heap_list[3], 40)
        bh.insert(50)
        self.assertEqual(bh.heap_list[4], 50)
        bh.insert(20)
        self.assertEqual(bh.heap_list[2], 20)
        self.assertEqual(bh.heap_list[5], 30)

    def test_find_min(self):
        bh = BinaryHeap()
        bh.insert(1)
        self.assertEqual(bh.find_min(), 1)

    def test__min_child(self):
        bh = BinaryHeap()
        bh.insert(1)
        bh.insert(5)
        bh.insert(6)
        bh.insert(2)
        bh.insert(3)
        bh.insert(4)
        self.assertEqual(bh._min_child(1), 2)
        self.assertEqual(bh._min_child(2), 5)

    def test_del_min(self):
        bh = BinaryHeap()
        bh.build_heap([4,1,7,3,5,2])
        self.assertEqual(bh.del_min(), 1)
        self.assertEqual(bh.heap_list, [0,2,3,7,4,5])

    def test_is_empty(self):
        bh = BinaryHeap()
        self.assertEqual(bh.is_empty(), True)
        bh.insert(1)
        self.assertEqual(bh.is_empty(), False)

    def test_size(self):
        bh = BinaryHeap()
        bh.insert(1)
        self.assertEqual(bh.size(), 1)
        bh.insert(99)
        self.assertEqual(bh.size(), 2)

    def test_build_heap(self):
        bh = BinaryHeap()
        bh.build_heap([4,1,7,3,5,2])
        self.assertEqual(bh.heap_list, [0,1,3,2,4,5,7])