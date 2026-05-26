class MinStack:

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, val: int) -> None:
        self.st.append(val)
        # self.min = min(self.min,val)
        val = min(val,self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        # if self.st[-1] == self.min:
        #     self.st.pop()
        #     self.min = min(self.st)
        # else:
        #     self.st.pop()
        self.st.pop()
        self.min.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]
