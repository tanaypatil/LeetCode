from collections import Counter


class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        if not arr:
            return 0
        counts = Counter(arr)
        m = 1
        for i, a in enumerate(arr):
            if counts[a]:
                p = a
                c = 1
                counts[a] -= 1
                while counts[p+1]:
                    c += 1
                    p += 1
                    counts[p] -= 1
                p = a
                while counts[p-1]:
                    c += 1
                    p -= 1
                    counts[p] -= 1
                m = max(m, c)
        return m
        