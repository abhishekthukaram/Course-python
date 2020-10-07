class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def isstackempty(self):
        return self.items == []

    def topofstack(self):
        if self.isstackempty():
            return self.items[-1]


def stringreverse(input_str):
    send = Stack()
    for i in input_str:
        send.push(i)
    output = ""
    count = len(input_str)
    while not send.isstackempty():
        output+=send.pop()
    return output
    """
    while count!=0:
        string_add= send.pop()
        output+=string_add
        count-=1
    return output
    """

print(stringreverse("Hello"))
print (stringreverse("Mountain"))