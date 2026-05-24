class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            if len(self.minstack) == 0:
                cur_min = val
            else:
                cur_min = min(val,self.minstack[-1])
            self.minstack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
