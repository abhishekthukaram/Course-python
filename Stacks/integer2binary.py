class Stack():
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def topofstack(self):
        return self.items[-1]

    def getstack(self):
        return self.items


def interger2binary(num):
    number = Stack()
    binary = ""
    while num>0:
        print num
        rem = num %2
        number.push(rem)
        num = num//2
    print (number.getstack())
    while not number.isempty():
        binary+=str(number.pop())
    return binary


print (interger2binary(242))