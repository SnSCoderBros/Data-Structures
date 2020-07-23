"""
Circular Linked Lists
"""


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
                prev.next = new_node
                new_node.next = cur
                return

            if cur == self.head:
                print("prev_data passed doesn't exist in the list")
                return

    def remove_fibonacci_nums(self):  # 0 1 1 2 3 5 8 13 21 34 55 89
        # find the largest number
        cur = self.head
        largest_num = cur.data

        while cur:
            cur = cur.next
            if cur == self.head:
                break

            if cur.data > largest_num:
                largest_num = cur.data

        # create fib_array
        fib_array = [0, 1]
        num = None

        while num < largest_num:
            last = fib_array[-1]
            second_to_last = fib_array[-2]

            num = last + second_to_last
            fib_array.append(num)

        # print(fib_array)

        # remove fib nodes

        prev = None
        cur2 = self.head
        old_head = self.head

        while cur2:
            if cur2.data in fib_array:
                if cur2 == self.head:
                    self.head = self.head.next
                    cur2 = self.head
                else:
                    nxt = cur2.next
                    prev.next = nxt
                    cur2 = nxt
            else:
                prev = cur2
                cur2 = cur2.next

            if cur2 == old_head:
                prev.next = self.head
                break


def is_circular_linked_list(ll):
    cur = ll.head

    while cur.next:
        cur = cur.next
        if cur == ll.head:
            return True

    return False


cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
# cll.print_list()

sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
# sll.print_list()

print(is_circular_linked_list(cll))
print(is_circular_linked_list(sll))
