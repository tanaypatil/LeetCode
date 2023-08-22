class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [0]*k
        def combi(pos, i):
            if pos == k:
                ans.add(tuple(nums[:]))
                return
            
            for j in range(i, n-k+pos+2):
                nums[pos] = j
                combi(pos+1, j+1)
                    
        ans = set()
        if n == k:
            ans.add(range(1, n+1))
        else:
            combi(0, 1)
        return ans
        