from bisect import bisect


class MedianFinder:

    def __init__(self):
        self.l = []
        

    def addNum(self, num: int) -> None:
        i = bisect(self.l, num)
        self.l.insert(i, num)
        # print(self.l)

    def findMedian(self) -> float:
        n = len(self.l)
        if n % 2:
            return self.l[n//2]
        return (self.l[n//2] + self.l[(n//2)-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()