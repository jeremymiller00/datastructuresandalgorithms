from unittest import TestCase
from trees.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(TestCase):
    def test_put(self):
        bst = BinarySearchTree()
        bst.put(4, "a")
        bst.put(8, "b")
        bst.put(1, "c")
        bst.put(2, "d")
        self.assertEqual(bst.root.left_child.right_child.key , 2)
        self.assertEqual(bst.root.right_child.key, 8)

    def test_get(self):
        bst = BinarySearchTree()
        bst.put(4, "a")
        bst.put(8, "b")
        bst.put(1, "c")
        bst.put(2, "d")
        self.assertEqual(bst.get(1), "c")
        self.assertEqual(bst.get(2), "d")
        self.assertEqual(bst.get(4), "a")
        self.assertEqual(bst.get(8), "b")

    def test_delete(self):
        bst = BinarySearchTree()
        bst.put(4, "a")
        bst.put(8, "b")
        bst.put(1, "c")
        bst.put(2, "d")
        self.assertRaises(KeyError, bst.get(9))
        bst.delete((1))
        self.assertEqual(bst.root.left_child.key, 2)