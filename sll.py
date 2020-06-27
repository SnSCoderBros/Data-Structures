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

   def reverse(self):
        """
        None 1 (head) -> 2 -> 3 -> 4 -> None
        None <- 1 <- 2 <- 3 <- 4 (head)
        """
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

   def delete(self, data):
        # handle if the list is empty
        if not self.head:
            print('List is empty.')
            return

        prev = None
        cur = self.head

        while cur:

            # handles for if the current node is a node to delete
            if cur.data == data:
                # handles if it is the head node
                if cur == self.head:
                    self.head = self.head.next
                    cur = self.head  # B

                else:
                    # handles if it is a node in the middle
                    nxt = cur.next
                    prev.next = nxt
                    del cur
                    cur = nxt

            # node is not a node to delete
            else:
                prev = cur
                cur = cur.next

    # how to find the length of a sll
    def __len__(self):
        count = 0
        cur = self.head
        # A > B > C > D > None

        while cur:
            count += 1
            cur = cur.next

        return count

    def merge(self, sll2):
        if not self.head:
            return sll2.head

        if not sll2.head:
            return self.head

        l1 = self.head
        l2 = sll2.head
        new_list = None

        if l1.data <= l2.data:
            new_list = l1
            l1 = l1.next

        elif l2.data < l1.data:
            new_list = l2
            l2 = l2.next

        while l1 and l2:
            if l1.data <= l2.data:
                new_list.next = l1
                l1 = l1.next
                new_list = new_list.next

            elif l2.data < l1.data:
                new_list.next = l2
                l2 = l2.next
                new_list = new_list.next

        if not l2:
            new_list.next = l1

        if not l1:
            new_list.next = l2

        return new_list

"""
sll = SinglyLinkedList()
sll.append(1)
sll.append(3)
sll.append(5)

sll2 = SinglyLinkedList()
sll2.append(2)
sll2.append(4)

sll.merge(sll2)
sll.print_list()
"""


"""
sll = SinglyLinkedList()
sll.append('A')
sll.append('B')
sll.append('C')
sll.append('D')
sll.append('E')
sll.print_list()
print("\n")
sll.reverse()
"""
