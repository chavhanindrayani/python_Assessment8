def check_stack_queue_operation(operation):
    stack = []
    queue = []
    stack_output = []
    queue_output = []
    
    for i in operation:
        if i.startswith("push"):
            val = i.split()[1]
            stack.append(val)
        elif i == "pop":
            if not stack:
                return False, "Stack underflow"
            stack_output.append(stack.pop())
        elif i.startswith("enqueue"):
            val = i.split()[1]
            queue.append(val)
        elif i == "dequeue":
            if not queue:
                return False, "Queue undeflow"
            queue_output.append(queue.pop(0))
        else:
            return False, f"Unknown operation: {i}"
        return True, {
            "Final stack outupt (LIFO)":
            stack_output,
            "Final queue output (FIFO)":
        }
        
        ops = [
            "push 1", "push 2", "pop", "push 3", "pop", "enqueue 4", "enqueue 5", "dequeue", "enqueue 6", "dequeue"
        ]
        
        result, output = check_stack_queue_operation(ops)
        if result:
            print("oeration are valid and maintaian order.")
            print(output)
        else:
            print("Error", output)
        