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

    def delete(self, data):

        if not self.head:
            print('List is empty.')
            return

        cur = self.head

        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.head = self.head.next
                else:
                    cur.prev.next = cur.next

                    if cur.next:
                        cur.next.prev = cur.prev

            cur = cur.next

    def reverse(self):
        # None >< A >< B >< C >< D > None
        # None >< D >< C >< B >< A > None

        prev = None
        cur = self.head

        while cur:
            nxt = cur.next
            cur.next = cur.prev

            # cur.next = B
            # cur.prev = None

            if cur.prev:
                cur.prev = cur.next

            prev = cur
            # cur = nxt
            cur = cur.next

        self.head = prev


dll = DLL()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('D')
dll.append('E')
dll.append(1)
dll.append(2)
dll.reverse()
dll.print_list()
