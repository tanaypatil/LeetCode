def pow(n, x):
    m = 10**9+7
    n = n%m
    if not x:
        return 1
    if x % 2:
        return (n * pow(n**2, (x-1)//2))%m
    return pow(n**2, x//2)%m


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m = 10**9+7
        if n % 2:
            return (pow(5, (n//2 + 1)) % m * pow(4, (n//2)) % m)%m
        return (pow(5, n//2)%m * pow(4, n//2)%m)%m