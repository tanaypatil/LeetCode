class Solution:
    def mergeSort(self, arr):
        n = len(arr)
        if n == 1:
            return arr
        
        mid = n // 2 if not n % 2 else n//2 + 1
        
        left_sorted = self.mergeSort(arr[:mid])
        right_sorted = self.mergeSort(arr[mid:])
        right_double = list(map(lambda x: x*2, right_sorted))
        left = right = 0
        sorted_arr = []
        while left < len(left_sorted) and right < len(right_sorted):
            if left_sorted[left] > right_sorted[right]:
                # Solution.inversion_count += len(left_sorted)-left
                sorted_arr.append(right_sorted[right])
                right += 1
            else:
                sorted_arr.append(left_sorted[left])
                left += 1
                
        while left < len(left_sorted):
            sorted_arr.append(left_sorted[left])
            left += 1
            
        while right < len(right_sorted):
            sorted_arr.append(right_sorted[right])
            right += 1
                
        left = right = 0      
        while left < len(left_sorted) and right < len(right_sorted):
            if left_sorted[left] > right_double[right]:
                Solution.inversion_count += len(left_sorted)-left
                # sorted_arr.append(right_sorted[right])
                right += 1
            else:
                # sorted_arr.append(left_sorted[left])
                left += 1
          
        # print(left_sorted, right_sorted, sorted_arr)
        return sorted_arr
    
    def reversePairs(self, nums: List[int]) -> int:
        Solution.inversion_count = 0
        self.mergeSort(nums)
        return Solution.inversion_count