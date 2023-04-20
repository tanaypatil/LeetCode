class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        arr = sorted(zip(startTime, endTime, profit), key=lambda x: (x[1], -x[2]))
        res = [[0, 0]]
        for start, end, p in arr:
            i = bisect.bisect(res, [start+1]) - 1
            if res[i][1] + p > res[-1][1]:
                res.append([end, p + res[i][1]])
        return res[-1][-1]
        