from collections import deque

class Queue:
    # value: list
    def __init__(self, value: list):
        self.value = deque(value)
    
    def push(self, item):
        self.value.append(item)
    
    def pop(self):
        return self.value.popleft()
    
    def pushpop(self, item):
        self.value.append(item)
        return self.value.popleft()
    
    def __call__(self):
        return self.value
    
    def __len__(self):
        return len(self.value)
    
    def size(self):
        return len(self.value)
    
    def empty(self):
        return len(self.value) == 0
    
    def front(self):
        return self.value[0]
    
    def back(self):
        return self.value(-1)
    
    def sorted(self):
        return deque(sorted(self.value))
