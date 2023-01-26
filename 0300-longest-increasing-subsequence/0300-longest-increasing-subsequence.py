class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        li = []
        m = 0
        for num in nums:
            if li and li[-1] >= num:
                index = bisect.bisect_left(li, num)
                li[index] = num
            else:
                li.append(num)
                m = max(m, len(li))
        return m