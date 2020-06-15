
"""

stack: []

append data: 1,2,3,4
[1,2,3,4]

pop data
[1,2,3]

functions

push()
pop()
is_empty()
__str__()
get_stack()
get_length()


"""


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def get_stack(self):
        return self.stack

    def get_length(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.get_stack())


# popped_num = stack.pop()

# print(stack)
# print(popped_num)
