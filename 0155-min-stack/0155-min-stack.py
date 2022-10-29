from collections import deque


class MinStack:

    def __init__(self):
        self.q=deque()
        # self.heap=[]
        self.minval=float('inf')
        # self.p=0
        
        
        

    def push(self, val: int) -> None:
        # heapq.heappush(self.heap,val)
        if not self.q:
            self.minval=val
        else:
            self.minval=min(self.q[0][1],val)
        # self.p=1
        
        self.q.appendleft((val,self.minval))
        

    def pop(self) -> None:
        self.q.popleft()
        # self.heap.remove(k)
        # heapq.heapify(self.heap)

    def top(self) -> int:
        return self.q[0][0]
        

    def getMin(self) -> int:
        return self.q[0][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()