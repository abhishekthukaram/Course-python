from collections import deque

class Node():
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

    def get_value(self):
        return self.value


tree = Node("Apple")
tree.left = Node("Banana")
tree.right = Node("Cherry")
tree.left.left = Node("Dates")


class Queue():
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.pop()
        else:
            return None

    def __len__(self):
        return len(self.queue)

#q= Queue()
#q.enqueue("Apple")
#q.enqueue("Banana")
#q.enqueue("Cherry")
#print q
#print q.dequeue()
#print q.dequeue()
#print q.dequeue()


def bfs(tree):
    q= Queue()
    visit_list = []
    if tree is None:
        return
    q.enqueue(tree)
    while len(q)>0:
        node = q.dequeue()
        #print node.value
        visit_list.append(node.value)
        if node.left is not None:
            q.enqueue(node.left)
        if node.right:
            q.enqueue(node.right)
    return visit_list


print(bfs(tree))


def printtree():
    level = 0
    

def detect_word(txt):
    result = ""
    for word in txt:
        if word is word.lower():
            result+=word
    return result


