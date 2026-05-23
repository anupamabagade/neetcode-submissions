class MinStack:

    def __init__(self):
        self.min_stack = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        # If stack empty
        if not self.stack:
            self.stack.append(0)
            self.min = val
        # If stack has elements in it 
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        # The real reason why we're appending the difference and not the value
        # If -ve value is popped, min of stack changes
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else: # If top value is -ve, top value is min
            return self.min

    def getMin(self) -> int:
        return self.min
        
