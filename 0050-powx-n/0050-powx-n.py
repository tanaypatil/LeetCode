class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not x:
            return 0
        if not n:
            return 1
        if n == 1:
            return x
        if n < 0:
            x = (1/x)
            n *= -1
        return x*self.myPow(x**2, (n-1)//2) if n&1 else self.myPow(x**2, n//2)