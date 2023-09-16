class Solution:
#     def merge(self, left, right):
#         merged = []
#         while left and right:
#             if left[-1][1] > right[-1][1]:
#                 Solution.res[left[-1][0]] += len(right)
#                 merged.append(left.pop())
#             else:
#                 merged.append(right.pop())
        
#         while left:
#             merged.append(left.pop())
        
#         while right:
#             merged.append(right.pop())
#         return merged
        
#     def merge_sort(self, nums):
#         if len(nums) == 1:
#             return nums
#         m = len(nums)//2
#         left = self.merge_sort(nums[:m])
#         right = self.merge_sort(nums[m:])
#         return self.merge(left, right)[::-1]

    def countSmaller(self, nums: List[int]) -> List[int]:
        # index_nums = [*enumerate(nums)]
        # Solution.res = [0]*len(nums)
        # self.merge_sort(index_nums)
        # return Solution.res
        min_in_nums = min(nums)
        fenwick_tree_size = 0
        if min_in_nums  < 0:
            for i in range(len(nums)):
                nums[i] += abs(min_in_nums)
                fenwick_tree_size = max(fenwick_tree_size, nums[i])
        else:
            fenwick_tree_size = max(nums)
        fenwick_tree = FenwickTree(fenwick_tree_size+1)
        res = [0]*(len(nums))
        for i in range(len(nums)-1, -1, -1):
            res[i] += fenwick_tree.query(nums[i])
            fenwick_tree.update(nums[i])
        return res
    
    
class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*n
        
    def update(self, num):
        num += 1
        while num < self.n:
            self.tree[num] += 1
            num += (num & -num)
            
    def query(self, num):
        ans = 0
        while num > 0:
            ans += self.tree[num]
            num -= (num & -num)
        return ans