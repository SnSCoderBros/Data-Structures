class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)


bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)

print(bt.root.data)
print(bt.root.left.data)
print(bt.root.right.data)
