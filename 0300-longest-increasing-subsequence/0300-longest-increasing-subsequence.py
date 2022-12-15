class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
#         def dfs(index, last, longest):
#             if index >= len(nums):
#                 return longest
            
#             not_taken = dfs(index+1, last, longest)
#             taken = float('-inf')
#             if not last or nums[index] > last:
#                 taken = 1+dfs(index+1, nums[index], longest)
#             return max(not_taken, taken)
#         return dfs(0, None, 0)
    
        # n = len(nums)
        # dp = [1]*n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1+dp[j])
        # return dp[-1]
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
            # print(sub)
        return len(sub)