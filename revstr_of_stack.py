#write a program to reverse a string using stack.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Push an item onto the stack.
        self.stack.append(item)

    def pop(self):
        # Pop an item from the stack.
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        # Return the top item without removing it.
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        # Check if the stack is empty.
        return len(self.stack) == 0

def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

string = "Ambission!"
rev_str = reverse_string(string)
print(f"Original String: {string}")
print(f"Reversed String: {rev_str}")
