class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        
        ret = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] <= ret[-1][1]:
                end = max(ret[-1][1], curr[1])
                ret[-1][1] = end
            else:
                ret.append(curr)
                
        return ret