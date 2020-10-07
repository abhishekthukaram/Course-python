class Node:
    def __init__(self , data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current_node = self.head
        while current_node:
            print (current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node .next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node .next = self.head
        self.head = new_node

    def insertatposition(self, data, prev_node):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        previous_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        current_node = self.head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        count = 1
        while current_node and count != pos:
            previous_node = current_node
            current_node = current_node.next
            count+=1
        if current_node is None:
            return "Position is greater"
        previous_node.next = current_node.next
        current_node = None

    def lengthofll_iterative(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count+=1
            current_node= current_node.next
        return count

    def lengthofll_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.lengthofll_recursive(node.next)

    def swapnodes(self, key1, key2):
        if key1 == key2:
            return
        prev_1 = None
        curr_1 = self.head

        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head

        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def swap_nodes_alter(self, key1, key2):
        if key1 == key2:
            return
        x, y = None
        current = self.head
        while current:
            if current.data == key1:
                x= current.data
            if current.data == key2:
                y = current.data
            current = current.next
        if x and y:
            x.data , y.data = y.data,x.data
        else:
            return

    '''Reverse a Linked List'''
    def llreverse(self):
        prev = None
        current = self.head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev

    '''Merge two sorted Linked List'''
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        '''check if either one of them is empty'''
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s= p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data<=q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        '''if one of them is ovr '''
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    '''Remove Duplicates in a Linked list'''
    def removeduplicates(self):
        dup = dict()
        current = self.head
        prev = None
        while current:
            if current.data in dup:
                prev.next = current.next
                current = None
            else:
                dup[current.data] = 1
                prev = current
            current = prev.next

    '''Kth Node from the last'''
    def printnodefrom_last(self, n):
        '''Method1'''
        length = self.lengthofll_iterative()
        current = self.head
        while current is not None:
            if length == n:
                print current.data
            length-=1
            current = current.next
        if current is None:
            return


ll = Linkedlist()
ll.append(1)
ll.append(2)
ll.append(2)
ll.append(4)
ll.append(5)
ll.printnodefrom_last(1)
"""
ll.append(4)
ll.removeduplicates()
ll.printlist()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
#print ll.lengthofll_iterative()
#print ll.lengthofll_recursive(ll.head)
#ll.swapnodes("A", "C")
ll.llreverse()
ll.printlist()
#ll.delete_node("B")
#ll.delete_node("E")
#print ll.delete_node_at_pos(2)
#ll.printlist()
#print (ll.head.next.data)
#ll.prepend("C")
#ll.insertatposition("E", ll.head.next)
#ll.prepend("C")
"""






