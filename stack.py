class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Top of the stack: {stack.peek()}")  # Output: 30
print(f"Stack size: {stack.size()}")        # Output: 3
print(f"Popped from stack: {stack.pop()}")  # Output: 30
print(f"Stack after pop: {stack.size()}")   # Output: 2