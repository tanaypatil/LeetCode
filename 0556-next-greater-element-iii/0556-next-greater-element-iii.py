class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1
        k = float('-inf')
        p = -1
        while i >= 0:
            j = i-1
            while j >= 0 and nums[j] >= nums[i]:
                j -= 1
            if j > k and j >= 0:
                k = j
                p = i
            i -= 1
        if k == float('-inf'):
            nums[:] = nums[::-1]
        else:
            nums[p], nums[k] = nums[k], nums[p]
            nums[k+1:] = nums[n-1:k:-1]
    
    def nextGreaterElement(self, n: int) -> int:
        if n >= 2**31:
            return -1
        print(2**31)
        nums = list(map(int, list(str(n))))
        next_num = nums[:]
        self.nextPermutation(next_num)
        ret = int(''.join(list(map(str, next_num))))
        if n >= ret or ret >= 2**31:
            return -1
        return ret