class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # print(nums)
        nums = [float('-inf')] + nums + [float('-inf')]
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m-1
            elif nums[m-1] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return -1
    
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        for i, r in enumerate(mat):
            c = self.findPeakElement(r)
            top = mat[i-1][c] if i > 0 else float('-inf')
            bot = mat[i+1][c] if i < m-1 else float('-inf')
            if mat[i][c] > top and mat[i][c] > bot:
                return [i, c]
            
        for j in range(n):
            c = self.findPeakElement([mat[i][j] for i in range(m)])
            left = mat[c][j-1] if j > 0 else float('-inf')
            right = mat[c][j+1] if j < n-1 else float('-inf')
            
            if mat[c][j] > left and mat[c][j] > right:
                return [c, j]
        return [-1, -1]