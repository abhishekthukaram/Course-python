from collections import deque


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None


q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)
print(q.deq())