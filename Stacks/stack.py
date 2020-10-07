class Stack():
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isempty():
            return self.items[-1]

    def isempty(self):
        return self.items == []

    def getstack(self):
        return self.items


s= Stack()
s.push("A")
s.push("B")
s.push("C")
s.pop()

print s.getstack()
print s.isempty()