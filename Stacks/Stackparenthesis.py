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


def checkmatch(param1,param2):
    if param1 == '{' and param2 == '}':
        return True
    elif param1 == '(' and param2 == ')':
        return True
    elif param1 == '[' and param2 == ']':
        return True
    else:
        return False


def checkparenthesis(letter):
    s = Stack()
    for i in letter:
        if i in "{([":
            s.push(i)
        else:
            if s.isempty():
                return False
            else:
                result = s.pop()
                if not checkmatch(result, i):
                    return False
    if s.isempty():
        return True
    else:
        return False


print checkparenthesis("}{}}")



