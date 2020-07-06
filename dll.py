"""
Doubly Linked Lists
- uses Nodes
None < A >< B >< C >< D > None 
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    def print_list(self):

        cur = self.head
        while cur:
            # if cur.prev:
            #     print(cur.prev.data)

            print(cur.data)

            # if cur.next:
            #     print(cur.next.data)

            cur = cur.next

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur

    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        old_head = self.head
        new_node.next = old_head
        old_head.prev = new_node
        self.head = new_node


dll = DLL()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')
dll.print_list()
