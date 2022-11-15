from bisect import bisect


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        temp = []
        if newInterval[0] < intervals[0][0]:
            temp.append(newInterval)
        temp.append(intervals[0])
            
        f = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] > newInterval[0]:
                temp.append(newInterval)
                f = 1
            temp.append(intervals[i])
        if not f:
            temp.append(newInterval)
        # print(temp)
        ret = [temp[0]]
        
        for i in range(1, len(temp)):
            if temp[i][0] <= ret[-1][1]:
                end = max(ret[-1][1], temp[i][1])
                ret[-1][1] = end
            else:
                ret.append(temp[i])
        
        return ret
        