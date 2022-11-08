class Solution:
    def atMostK(self, nums, K):
        res = 0
        left = 0
        counts = Counter()
        for right, num in enumerate(nums):
            if not counts[num]:
                K -= 1
            counts[num] += 1
            while K < 0:
                counts[nums[left]] -= 1
                if not counts[nums[left]]:
                    K += 1
                left += 1
            res += right-left+1
        return res
    
    
    def numberOfSubstrings(self, s: str) -> int:
        # left, right = 0, 0
        # count = 0
        # freq = {}
        # for right, c in enumerate(s):
        #     freq[c] = freq.get(c, 0) + 1
        #     while len(freq) >= 3:
        #         freq[s[left]] -= 1
        #         if freq[s[left]] == 0:
        #             del freq[s[left]]
        #         left += 1
        #     count += left
        # return count
        
        return self.atMostK(s, 3) - self.atMostK(s, 2)