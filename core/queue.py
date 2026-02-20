from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue=deque()

    def enqueue(self,task):
        self.queue.append(task)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None
    
    def isEmpty(self):
        return len(self.queue)==0