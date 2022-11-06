class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        max_count = 0
        freq = {}
        for end in range(len(s)):
            freq[s[end]] = freq.get(s[end], 0) + 1
            
            window_len = end-start+1
            replacement_cost = window_len - max(freq.values())
            if replacement_cost <= k:
                max_count = max(max_count, window_len)
            else:
                freq[s[start]] -= 1
                start += 1
        return max_count
        