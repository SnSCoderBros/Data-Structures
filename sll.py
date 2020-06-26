'''
Nodes:
data, next

data -> 'A'
next -> Node that holds the data element 'B'

A -> B -> C -> D -> None
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    # based around the concept of Nodes
    # creates a chain of Nodes by connecting them with one another

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # handle for if the list is empty
        if not self.head:
            self.head = new_node
            return

        # handle for if the list is not empty
        cur_node = self.head

        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def print_list(self):
        # A -> B -> C -> None
        # self.head = "A" -> self.head -> "B" -> self.head -> "C"... -> self.head -> None

        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        # add a node at the very start
        new_node = Node(data)

        # handle if the list is empty
        if not self.head:
            self.head = new_node
            return

        # handle if the list is not empty
        old_head = self.head
        self.head = new_node
        self.head.next = old_head

    def insert(self, prev_node, data):
        # A -> B -> C -> D -> E -> None
        # A -> B -> new -> C -> D -> E -> None

        new_node = Node(data)
        cur = self.head

        while cur and cur != prev_node:
            cur = cur.next

        if not cur:
            return

        nxt = cur.next
        cur.next = new_node
        new_node.next = nxt


sll = SinglyLinkedList()
sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')
sll.append('E')
sll.insert(sll.head.next, 'new')
sll.print_list()
