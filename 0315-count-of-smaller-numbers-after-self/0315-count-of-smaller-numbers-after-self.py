class Solution:
    def merge(self, left, right):
        merged = []
        while left and right:
            if left[-1][1] > right[-1][1]:
                Solution.res[left[-1][0]] += len(right)
                merged.append(left.pop())
            else:
                merged.append(right.pop())
        
        while left:
            merged.append(left.pop())
        
        while right:
            merged.append(right.pop())
        return merged
        
    def merge_sort(self, nums):
        if len(nums) == 1:
            return nums
        m = len(nums)//2
        left = self.merge_sort(nums[:m])
        right = self.merge_sort(nums[m:])
        return self.merge(left, right)[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        index_nums = [*enumerate(nums)]
        Solution.res = [0]*len(nums)
        self.merge_sort(index_nums)
        return Solution.res