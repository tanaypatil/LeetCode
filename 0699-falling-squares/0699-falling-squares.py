class Solution:
    def fallingSquares(self, A: List[List[int]]) -> List[int]:
        dp = [0] * len(A)
        for i in range(len(A)):
            for j in range(i, -1, -1):
                if A[i][0] <= A[j][0] < A[i][0] + A[i][1] or A[j][0] <= A[i][0] < A[j][0] + A[j][1]:
                    dp[i] = max(dp[i], A[i][1] + dp[j])
        return accumulate(dp, func=max)