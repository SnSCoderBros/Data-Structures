"""
Circular Linked Lists
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# list keeps circling around on itself
# A > B > C > D > A > B > C...


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def append(self, data):
        new_node = Node(data)

        # if the list is empty
        if not self.head:
            self.head = new_node
            self.head.next = self.head

        # if list is not empty
        cur = self.head
        while cur:
            if cur.next == self.head:
                break
            cur = cur.next

        cur.next = new_node
        new_node.next = self.head

    def prepend(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            return
        new = Node(data)
        # A -> B -> C -> D -> A
        orig_head = self.head
        new.next = orig_head
        self.head = new
        last = orig_head
        while last.next != orig_head:
            last = last.next
        last.next = self.head

    def delete(self, data):

        if self.head.data == data:
            cur = self.head
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = cur.next
            self.head = last.next
            return
        prev = None
        cur = self.head
        while cur.next != self.head and cur.data != data:
            prev = cur
            cur = cur.next
        if cur.data == data:
            prev.next = cur.next
            cur = None


cll = CircularLinkedList()

cll.append('B')
cll.append('C')
cll.append('D')
cll.prepend("A")

cll.delete("B")

cll.print_list()
