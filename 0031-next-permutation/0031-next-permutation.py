def reverse(nums):
    i = 0
    n = len(nums)
    for i in range(((n-1)//2)+1):
        nums[i], nums[n-i-1] = nums[n-i-1], nums[i]


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        p = -1
        k = -1
        while i > 0:
            j = i-1
            while j != -1 and nums[j] >= nums[i]:
                j -= 1
            if j != -1:
                if j > p:
                    p = j
                    k = i
            i -= 1
        if p == -1:
            reverse(nums)
        else:
            nums[k], nums[p] = nums[p], nums[k]
            nums[p+1:] = list(reversed(nums[p+1:]))
        