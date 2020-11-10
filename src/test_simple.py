from unittest import TestCase
from simple import Stack, Queue, Deque

class TestStack(TestCase):
    def test_push(self):
        s = Stack()
        self.assertEqual(len(s.items), 0, "Failed Init")
        s.push(5)
        self.assertRaises(ValueError, s.push, "g")
        self.assertRaises(ValueError, s.push, {4, 5, 6})

    def test_pop(self):
        s = Stack()
        self.assertEqual(len(s.items), 0, "Failed Init")
        s.push(5)
        s.push(6)
        s.push(7)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 6)
        self.assertEqual(s.pop(), 5)
        self.assertRaises(AttributeError, s.pop)

    def test_peek(self):
        s = Stack()
        self.assertEqual(len(s.items), 0, "Failed Init")
        self.assertRaises(AttributeError, s.peek)
        s.push(5)
        s.push(6)
        s.push(7)
        self.assertEqual(s.peek(), 7)
        self.assertEqual(s.peek(), 7)

    def test_is_empty(self):
        s = Stack()
        self.assertEqual(len(s.items), 0, "Failed Init")
        self.assertEqual(s.isEmpty(), True)
        s.push(5)
        self.assertEqual(s.isEmpty(), False)
        s.pop()
        self.assertEqual(s.isEmpty(), True)

    def test_size(self):
        s = Stack()
        self.assertEqual(len(s.items), 0, "Failed Init")
        self.assertEqual(s.size(), 0)
        s.push(5)
        self.assertEqual(s.size(), 1)
        s.push(6)
        self.assertEqual(s.size(), 2)
        s.push(7)
        self.assertEqual(s.size(), 3)
        s.pop()
        self.assertEqual(s.size(), 2)


class TestQueue(TestCase):
    def test_enqueue(self):
        q = Queue()
        self.assertEqual(len(q.items), 0, "Failed Init")
        q.enqueue(5)
        self.assertRaises(ValueError, q.enqueue, "g")
        self.assertRaises(ValueError, q.enqueue, {4, 5, 6})

    def test_dequeue(self):
        q = Queue()
        self.assertEqual(len(q.items), 0, "Failed Init")
        q.enqueue(5)
        q.enqueue(6)
        q.enqueue(7)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 6)
        self.assertEqual(q.dequeue(), 7)
        self.assertRaises(AttributeError, q.dequeue)

    def test_is_empty(self):
        q = Queue()
        self.assertEqual(len(q.items), 0, "Failed Init")
        self.assertEqual(q.isEmpty(), True)
        q.enqueue(5)
        self.assertEqual(q.isEmpty(), False)
        q.dequeue()
        self.assertEqual(q.isEmpty(), True)

    def test_size(self):
        q = Queue()
        self.assertEqual(len(q.items), 0, "Failed Init")
        self.assertEqual(q.size(), 0)
        q.enqueue(5)
        self.assertEqual(q.size(), 1)
        q.enqueue(5)
        self.assertEqual(q.size(), 2)
        q.enqueue(7)
        self.assertEqual(q.size(), 3)
        q.dequeue()
        self.assertEqual(q.size(), 2)


class TestDeque(TestCase):
    def test_add_front(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        d.addFront(5)
        d.addFront(6)
        self.assertEqual(d.items[0], 6)
        self.assertRaises(ValueError, d.addFront, "g")
        self.assertRaises(ValueError, d.addFront, {4, 5, 6})

    def test_add_rear(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        d.addRear(5)
        d.addRear(6)
        self.assertEqual(d.items[0], 5)
        self.assertRaises(ValueError, d.addFront, "g")
        self.assertRaises(ValueError, d.addFront, {4, 5, 6})

    def test_remove_front(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        d.addFront(5)
        d.addRear(6)
        d.addFront(7)
        self.assertEqual(d.removeFront(), 7)
        self.assertEqual(d.removeFront(), 5)
        self.assertEqual(d.removeFront(), 6)
        self.assertRaises(AttributeError, d.removeFront)

    def test_remove_rear(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        d.addFront(5)
        d.addRear(6)
        d.addFront(7)
        self.assertEqual(d.removeRear(), 6)
        self.assertEqual(d.removeRear(), 5)
        self.assertEqual(d.removeRear(), 7)
        self.assertRaises(AttributeError, d.removeRear)

    def test_is_empty(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        self.assertEqual(d.isEmpty(), True)
        d.addFront(5)
        self.assertEqual(d.isEmpty(), False)
        d.removeRear()
        self.assertEqual(d.isEmpty(), True)

    def test_size(self):
        d = Deque()
        self.assertEqual(len(d.items), 0, "Failed Init")
        self.assertEqual(d.size(), 0)
        d.addFront(5)
        self.assertEqual(d.size(), 1)
        d.addRear(5)
        self.assertEqual(d.size(), 2)
        d.removeFront()
        self.assertEqual(d.size(), 1)
        d.removeRear()
        self.assertEqual(d.size(), 0)
