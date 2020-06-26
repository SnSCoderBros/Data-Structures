
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


# stack = Stack()

# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(stack.get_stack())

# popped_num = stack.pop()

# print(stack)
# print(popped_num)

'''
Use a stack to check whether or not a string is balanced.

(), ([{}]) <-- Balanced
()), ()(]), ({) <-- Unbalanced
'''


def balance_paranthesis(parens):
    if len(parens) <= 1:
        return False

    s2 = Stack()
    paren_dict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for paren in parens:
        # handle if paren is opening
        if paren in paren_dict.keys():
            s2.push(paren)

        # handle if paren in closing
        if paren in paren_dict.values():
            open_bracket = s2.peek()
            if paren_dict[open_bracket] != paren:
                return False
            else:
                s2.pop()

    return True


# string = "([{}])"  # should return True
string = "()(])"  # should return False

boolean = balance_paranthesis(string)
print(boolean)
