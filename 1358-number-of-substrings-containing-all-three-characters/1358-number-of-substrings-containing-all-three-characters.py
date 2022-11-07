class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, right = 0, 0
        count = 0
        freq = {}
        for right, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1
            while len(freq) >= 3:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            count += left
        return count