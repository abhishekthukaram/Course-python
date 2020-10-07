import unittest


def contains_cycle(first_node):

    # Check if the linked list contains a cycles
    slow_node= first_node
    fast_node=first_node
    while True:
        if slow_node != None and fast_node.next!=None:
            slow_node=slow_node.next
            fast_node=fast_node.next.next
        else:
            return False
        if fast_node == None or slow_node == None:
            return False
        elif slow_node.value == fast_node.value:
            return True


print(contains_cycle())
