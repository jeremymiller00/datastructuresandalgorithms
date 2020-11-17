'''
Simple data structures: stack, queue, deque
'''

class Stack(object):
    '''
    Basic implementation of stack data structure
    LIFO
    A stack should have a single data type
    '''

    def __init__(self):
        '''
        Create a new stack instance
        '''
        self.items = []
        self.datatype = None

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    def push(self, x):
        '''
        Add an item to the stack
        :param x: item {any, or list}
        :return: None
        '''
        if self.datatype is not None and not isinstance(x, self.datatype):
            raise ValueError(f"Invalid data type for object. Data type must be {self.datatype}")
        self.items.append(x)
        if len(self.items) == 1:
            self.datatype = type(x)

    def pop(self):
        '''
        Remove and return item on top of stack
        :return: updated stack {list}
        '''
        if len(self.items) == 0:
            raise AttributeError("Empty stack")
        last = self.items[-1]
        self.items = self.items[:-1]
        return last

    def peek(self):
        '''
        Get item on top of the stack without removing it
        :return: top item {any}
        '''
        if len(self.items) == 0:
            raise AttributeError("Empty stack")
        return self.items[-1]

    def is_empty(self):
        '''
        True if the stack is empty, false otherwise
        :return: bool
        '''
        return len(self.items) == 0

    def size(self):
        '''
        Wrapper for length
        :return: int
        '''
        return len(self.items)


class Queue(object):
    '''
    Basic queue structure
    FIFO
    A queue should have a single data type
    '''

    def __init__(self):
        '''
        Create new queue instance
        '''
        self.items = []
        self.datatype = None

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    def enqueue(self, x):
        '''
        Add item to queue
        :param x: item to add {any}
        :return: None
        '''
        if self.datatype is not None and not isinstance(x, self.datatype):
            raise ValueError(f"Invalid data type for object. Data type must be {self.datatype}")
        self.items.insert(0, x)
        if len(self.items) == 1:
            self.datatype = type(x)

    def dequeue(self):
        '''
        Remove and return first item inserted into queue
        :return: queue item {any}
        '''
        if len(self.items) == 0:
            raise AttributeError("Empty stack")
        last = self.items[-1]
        self.items = self.items[:-1]
        return last

    def is_empty(self):
        '''
        True if queue is empty, false otherwise
        :return: bool
        '''
        return len(self.items) == 0

    def size(self):
        '''
        Wrapper for length
        :return: int
        '''
        return len(self.items)


class Deque(object):
    '''
    Basic double ended queue
    Can add to or pull from either end
    A queue should have a single data type
    '''

    def __init__(self):
        '''
        Create new dequeue instance
        '''
        self.items = []
        self.datatype = None

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

    def add_front(self, x):
        '''
        Add an item to the front of the dequeue
        :param x: added item {any}
        :return: None
        '''
        if self.datatype is not None and not isinstance(x, self.datatype):
            raise ValueError(f"Invalid data type for object. Data type must be {self.datatype}")
        self.items.insert(0, x)
        if len(self.items) == 1:
            self.datatype = type(x)

    def add_rear(self, x):
        '''
        Add an item to the rear of the queue
        :param x: item {any, or list}
        :return: None
        '''
        if self.datatype is not None and not isinstance(x, self.datatype):
            raise ValueError(f"Invalid data type for object. Data type must be {self.datatype}")
        self.items.append(x)
        if len(self.items) == 1:
            self.datatype = type(x)

    def remove_front(self):
        '''
        Remove and return first item in dequeue
        :return: updated stack {list}
        '''
        if len(self.items) == 0:
            raise AttributeError("Empty dequeue")
        front = self.items[0]
        self.items = self.items[1:]
        return front

    def remove_rear(self):
        '''
        Remove and return last item in dequeue
        :return: queue item {any}
        '''
        if len(self.items) == 0:
            raise AttributeError("Empty dequeue")
        rear = self.items[-1]
        self.items = self.items[:-1]
        return rear

    def is_empty(self):
        '''
        True if dequeue is empty, False otherwise
        :return: bool
        '''
        return len(self.items) == 0

    def size(self):
        '''
        Wrapper for length function
        :return: int
        '''
        return len(self.items)