class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0: 
            return 0
        N = list(map(int, str(n)))

        @functools.lru_cache(None)
        def dp(pos, isPrefix, isBigger, ones):
            if pos == len(N):
                return 0
            result = 0
            for i in range(0 if pos > 0 else 1, 10):
                _isPrefix = isPrefix and i == N[pos]
                _isBigger = isBigger or (isPrefix and i > N[pos])
                _ones = ones + (1 if i == 1 else 0)
                if not (pos == len(N) - 1 and _isBigger):
                    result += ones
                if i == 1 and not (pos == len(N) - 1 and _isBigger):
                    result += 1
                result += dp(pos + 1, _isPrefix, _isBigger, _ones)
            return result

        return dp(0, True, False, 0)
        