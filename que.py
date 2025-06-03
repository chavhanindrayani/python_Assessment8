# 3.	Queue:
# o	Implement a queue that accepts strings and provides the methods enqueue(), dequeue(), and size().

class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
queue = Queue()
queue.enqueue("python")
queue.enqueue("java")

print(f"Dequeued : {queue.size()}")
print(f"Dequeued : {queue.dequeue()}")
print(f"Dequeued : {queue.dequeue()}")
