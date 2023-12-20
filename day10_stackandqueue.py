#day10 lc 232, and lc 225
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack2:
            return self.stack2.pop()
        else:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

            return self.stack2.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack2.append(ans)
        return ans

    def empty(self) -> bool:
        if self.stack1 or self.stack2:
            return False
        else:
            return True

class MyStack:

    def __init__(self):
        self.que1 = deque()

    def push(self, x: int) -> None:
        self.que1.append(x)



    def pop(self) -> int:
        if not self.que1:
            return self.que1
        ans = self.que1.pop()
        return ans


    def top(self) -> int:
        if not self.que1:
            return self.que1
        
        return self.que1[-1]

    def empty(self) -> bool:
        if not self.que1:
            return True 
        return False
