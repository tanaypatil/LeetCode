class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        index_map = {v:k for k, v in enumerate(row)}
        swaps = 0
        
        def swap(i, j):
            row[i], row[j] = row[j], row[i]
            index_map[row[i]] = i
            index_map[row[j]] = j
        
        for i in range(0, len(row), 2):
            first = row[i]
            second = first ^ 1
            
            if row[i+1] != second:
                swaps += 1
                swap(i+1, index_map[second])
                
        return swaps
            
            