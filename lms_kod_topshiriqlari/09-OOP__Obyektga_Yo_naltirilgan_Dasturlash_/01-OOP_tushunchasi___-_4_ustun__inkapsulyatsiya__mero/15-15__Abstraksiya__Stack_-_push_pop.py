class Stack:
    def __init__(self):
        self._items = []
    def push(self, x):
        self._items.append(x)
    def pop(self):
        if self._items:
            return self._items.pop()
        return None
    def size(self):
        return len(self._items)
    
numbers = list(map(int, input().split()))

stack = Stack()

for num in numbers:
    stack.push(num)
    
popped_val = stack.pop()
remaining_size = stack.size()

print(f"{popped_val} {remaining_size}")