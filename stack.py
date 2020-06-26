
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

    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)



"""
Here we test if the stack works

# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.get_stack())

# popped_num = stack.pop()

# print(stack)
# print(popped_num)


"""



















"""
Here we implement the Queue with 2 stacks

How a queue works
1,2
[1] => [1,2] => [2], 1 => [] 2

with 2 stacks
1
[1] []

2
[1,2] []

now we want to pop (1)
[1,2] [] => [1] [2]  => [] [2,1] => [] [2] 1 => [2] []

push()
pop()
length()



class Queue:

    def __init__(self):
        self.orig = Stack()
        self.copy = Stack()

    def push(self,data):
        self.orig.push(data)
    
    def length(self):
        return self.orig.get_length()

    def pop(self):
        # [1] []
        if self.length() == 0:
            return
        if self.length() == 1:
            return self.orig.pop()
        # [1,2,3] [] => [1,2] [3] => [1] [3,2] => [] [3,2,1] => [] [3,2] 1 => [2] [3] 1 => [2,3] [] 1
        while not self.orig.is_empty():
            self.copy.push(self.orig.pop())
        popped_val = self.copy.pop()
        while not self.copy.is_empty():
            self.orig.push(self.copy.pop())
        return popped_val

    def __str__(self):
        return str(self.orig)

queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue)

print(queue.pop())
print(queue)

print(queue.pop())
print(queue)

print(queue.pop())
print(queue)

"""







'''
Use a stack to check whether or not a string is balanced.

(), ([{}]) <-- Balanced
()), ()(]), ({) <-- Unbalanced


# def balance_paranthesis(parens):
#     if len(parens) <= 1:
#         return False

#     s2 = Stack()
#     paren_dict = {
#         '(': ')',
#         '[': ']',
#         '{': '}'
#     }

#     for paren in parens:
#         # handle if paren is opening
#         if paren in paren_dict.keys():
#             s2.push(paren)

#         # handle if paren in closing
#         if paren in paren_dict.values():
#             open_bracket = s2.peek()
#             if paren_dict[open_bracket] != paren:
#                 return False
#             else:
#                 s2.pop()

#     return True


# string = "([{}])"  # should return True
# string = "()(])"  # should return False

# boolean = balance_paranthesis(string)
# print(boolean)
