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

        prev = None
        cur = self.head

        while cur:
            nxt = cur.next
            cur.next = cur.prev

            if cur.prev:
                cur.prev = cur.next

            prev = cur
            cur = nxt

        self.head = prev

    def is_palindrome(self):
        cur = self.head
        last = self.head

        while last.next:
            last = last.next

        while cur != last:
            # print(cur.data, last.data)

            if cur.data != last.data:
                return False

            cur = cur.next
            if cur == last:
                return True

            last = last.prev

        return True


dll = DLL()
dll.append('A')
dll.append('B')
dll.append('C')
dll.append('C')
dll.append('B')
dll.append('A')
print(dll.is_palindrome())
