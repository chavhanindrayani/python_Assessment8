# Create a priority queue that accepts tuples in the format (priority, value) and dequeues the highest priority first.

class Priority_Queue:
    def __init__(self):
        self.queue = []
        self.intdex = 0
        
    def enqueue(self, priority, value):
        self.queue.append