class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k: return False
        heapify(nums)
        counts = Counter(nums)
        for i in range((len(nums)//k)):
            first = -1
            for j in range(k):
                if not j:
                    while nums:
                        first = heappop(nums)
                        if counts[first]: 
                            counts[first] -= 1
                            break
                    if first == -1: 
                        return False
                else:
                    if not counts[first+j]: return False
                    counts[first+j] -= 1
                    
        return True