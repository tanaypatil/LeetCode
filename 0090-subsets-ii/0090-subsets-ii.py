class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        for i in range(0, 2**n):
            bits = bin(i)[2:]
            bits = "0"*(n-len(bits)) + bits
            curr = []
            for j in range(n):
                if bits[j] == "1":
                    curr.append(nums[j])
            ans.add(tuple(curr))
        return list(map(list, ans))
        