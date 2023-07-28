class Solution:
    def get_median(self, max_heap, min_heap, k):
        if k & 1:
            return -max_heap[0][0]
        return (-max_heap[0][0] + min_heap[0][0]) / 2.0
    
    def move(self, from_heap, to_heap):
        num, idx = heappop(from_heap)
        heappush(to_heap, (-num, idx))
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        min_heap, max_heap, medians = [], [], []
        
        for i in range(k):
            heappush(max_heap, (-nums[i], i))
        for _ in range(k//2):
            num, idx = heappop(max_heap)
            heappush(min_heap, (-num, idx))
            
        medians.append(self.get_median(max_heap, min_heap, k))
        
        for i in range(k, len(nums)):
            if not max_heap or nums[i] <= -max_heap[0][0]:
                heappush(max_heap, (-nums[i], i))
                if min_heap and nums[i-k] >= min_heap[0][0]:
                    self.move(max_heap, min_heap)
            else:
                heappush(min_heap, (nums[i], i))
                if max_heap and nums[i-k] <= -max_heap[0][0]:
                    self.move(min_heap, max_heap)
                    
            while max_heap and max_heap[0][1] <= i-k:
                heappop(max_heap)
            while min_heap and min_heap[0][1] <= i-k:
                heappop(min_heap)
                
            medians.append(self.get_median(max_heap, min_heap, k))
            
        return medians