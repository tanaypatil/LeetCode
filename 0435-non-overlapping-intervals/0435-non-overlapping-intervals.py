class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        count = 0
        intervals.sort(key=lambda x: (x[0], x[1]))
        # print(intervals)
        ret = [intervals[0]]
        for i in range(1, len(intervals)):
            if ret[-1][1] > intervals[i][0]:
                count += 1
                # ret[-1][1] = max(ret[-1][1], intervals[i][1])
                if intervals[i][1] < ret[-1][1]:
                    ret[-1][0], ret[-1][1] = intervals[i]
            else:
                ret.append(intervals[i])
                
        return count
        