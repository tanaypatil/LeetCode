class Solution:
    def countPrimes(self, n: int) -> int:
        if n in (0, 1, 2):
            return 0
        
        sieve = [1]*n
        sieve[:2] = [0, 0]
        ans = 0
        sqt = int(sqrt(n))
        for i in range(2, sqt+1):
            if sieve[i]:
                for j in range(i, (n//i)+1):
                    if i*j < n:
                        sieve[i*j] = 0
            ans += 1 if sieve[i] else 0
        for i in range(sqt+1, n):
            ans += 1 if sieve[i] else 0
        return ans