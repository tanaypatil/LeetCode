class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(m):
                while c >= 0 and ((r+1) * (c+1)) > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt

        left, right = 1, m*n
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1  # try to looking for a smaller value in the left side
            else:
                left = mid + 1  # try to looking for a bigger value in the right side

        return ans