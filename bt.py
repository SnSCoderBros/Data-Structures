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

print(bt.inorder_traversal())  # 4-2-5-1-6-3-7-
