class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        ret = []
        for i in range(len(pos)):
            ret.append(pos[i])
            ret.append(neg[i])
        return ret
        