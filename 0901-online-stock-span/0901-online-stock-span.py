class StockSpanner:

    def __init__(self):
        self.stack = [0]
        self.nums = [float('inf')]

    def next(self, price: int) -> int:
        while self.stack and self.nums[self.stack[-1]] <= price:
            self.stack.pop()
        ans = len(self.nums)-self.stack[-1]
        self.stack.append(len(self.nums))
        self.nums.append(price)
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)