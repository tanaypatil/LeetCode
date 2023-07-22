class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]
        i = j = 0
        ret = []
        c = 0
        while i < len(pos) and j < len(neg):
            if c & 1:
                ret.append(neg[j])
                j += 1
            else:
                ret.append(pos[i])
                i += 1
            c += 1
        while i < len(pos):
            ret.append(pos[i])
            i += 1
        while j < len(neg):
            ret.append(neg[j])
            j += 1
        return ret
        