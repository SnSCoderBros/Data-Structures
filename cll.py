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

    def __len__(self):
        if not self.head:
            return 0

        cur = self.head
        count = 1

        while cur.next != self.head:
            cur = cur.next
            count += 1

        return count

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

    def insert(self, prev_data, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return

        prev = None
        cur = self.head

        while cur:
            prev = cur
            cur = cur.next

            if prev.data == prev_data:
                break

            if cur == self.head:
                print('prev_data doesnt exist in the list')
                return

        prev.next = new_node
        new_node.next = cur


cll = CircularLinkedList()


cll.append('A')
cll.append('B')
cll.append('C')
cll.append('A')
cll.append('B')
cll.append('C')
cll.append('D')
print(len(cll))
# cll.print_list()
