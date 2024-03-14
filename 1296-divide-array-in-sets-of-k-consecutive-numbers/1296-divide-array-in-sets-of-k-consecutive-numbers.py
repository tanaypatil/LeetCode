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
                        # print("here1")
                        return False
                    # print(i, j, first)
                else:
                    if counts[first+j]:
                        counts[first+j] -= 1
                    else: 
                        # print("here2")
                        return False
        return True