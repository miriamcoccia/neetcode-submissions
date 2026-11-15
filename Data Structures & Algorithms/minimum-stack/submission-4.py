class MinStack:

    def __init__(self):
        self.stack = []
        self.minima = []        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minima) == 0:
            self.minima.append(val)
        elif val <= self.minima[-1]:
            self.minima.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minima[-1]:
           self.minima.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minima[-1] if self.minima else 0
