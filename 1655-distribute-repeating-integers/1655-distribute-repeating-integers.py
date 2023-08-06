class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        num_people = len(quantity)
        quantity.sort(reverse=True)
        counts = defaultdict(int, Counter(Counter(nums).values()))
        n = len(counts)
        
        
        def dp(i=0):
            if i == num_people: return True
            for freq, count in list(counts.items()):
                if freq >= quantity[i] and count > 0:
                    counts[freq] -= 1
                    counts[freq - quantity[i]] += 1
                    if dp(i+1): return True
                    counts[freq] += 1
                    counts[freq - quantity[i]] -= 1
            return False
        return dp()