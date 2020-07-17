class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def inorder_traversal(self):  # left, parent, right
        string = ''
        return self.inorder_helper(string, self.root)

    def inorder_helper(self, string, node):
        if node:
            string = self.inorder_helper(string, node.left)
            string += str(node.data) + '-'
            string = self.inorder_helper(string, node.right)

        return string

    def preorder_traversal(self):
        string = ''
        return self.preorder_helper(string, self.root)

    def preorder_helper(self, string, node):
        if node:
            string += str(node.data) + '-'
            string = self.preorder_helper(string, node.left)
            string = self.preorder_helper(string, node.right)

        return string

    def postorder_traversal(self):
        string = ''
        return self.postorder_helper(string, self.root)

    def postorder_helper(self, string, node):
        if node:
            string = self.postorder_helper(string, node.left)
            string = self.postorder_helper(string, node.right)
            string += str(node.data) + '-'

        return string


# 1 - 2 - 4 - 5 - 3 - 6 - 7 -  -> Pre order
# Post order -> 4 - 5 - 2 - 6 - 7 - 3 - 1
"""
            1
        2       3
      4   5    6  7
"""

bt = BinaryTree(1)
bt.root.left = Node(2)
bt.root.right = Node(3)
bt.root.left.left = Node(4)
bt.root.left.right = Node(5)
bt.root.right.left = Node(6)
bt.root.right.right = Node(7)

# print(bt.inorder_traversal())
# print(bt.preorder_traversal())
print(bt.postorder_traversal())
