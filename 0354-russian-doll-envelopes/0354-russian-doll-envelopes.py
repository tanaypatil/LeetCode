class Solution:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        arr.sort(key=lambda x: (x[0], -x[1]))
        a = [arr[0][1]]
        ans = 1
        for i in range(1, len(arr)):
            if arr[i][1] > a[-1]:
                a.append(arr[i][1])
            else:
                a[bisect_left(a, arr[i][1])] = arr[i][1]
            ans = max(ans, len(a))
        return ans
        