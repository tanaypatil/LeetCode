def power(x, n):
    if not x:
        return 0
    if not n:
        return 1
    n = n
    if n%2:
        return x*power(x**2, (n-1)//2)
    return power(x**2, n//2)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return power(x, n) if n >= 0 else power(1/x, -1*n)
        