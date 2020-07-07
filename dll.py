"""
Doubly Linked Lists
- uses Nodes
None < A >< B >< C >< D >< E > None 
'E'

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

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

    def print_list(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next

    def delete(self, data)
    pass


dll = DLL()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')
dll.print_list()
