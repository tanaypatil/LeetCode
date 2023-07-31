class Solution:
    def dfs(self, i, c, curr, arr, sdict):
        if i == len(arr):
            sdict[c].append(curr)
            return
        
        self.dfs(i+1, c+1, curr+arr[i], arr, sdict)
        self.dfs(i+1, c, curr, arr, sdict)
        
    def minimumDifference(self, nums: List[int]) -> int:
        sdict2 = defaultdict(list)
        total = sum(nums)
        n, target = len(nums)//2, total//2
        
        # self.dfs(0, 0, 0, nums[:n], sdict1)
        # self.dfs(0, 0, 0, nums[n:], sdict2)
        
        l_iter, r_iter = [(0, 0)], [(0, 0)] # (No. of numbers, sum)
		
		# Build Lft and Rgt
        for a in nums[:n]:
            cur = []
            for pre_num, pre_sum in l_iter:
                cur.append((pre_num, pre_sum))
                cur.append((pre_num + 1, pre_sum + a))
            l_iter = cur[:]
        for a in nums[n:]:
            cur = []
            for pre_num, pre_sum in r_iter:
                cur.append((pre_num, pre_sum))
                cur.append((pre_num + 1, pre_sum + a))
            r_iter = cur[:]
            
        for num, s in r_iter:
            sdict2[num].append(s)
        for key in sdict2.keys():
            sdict2[key] = sorted(sdict2[key])
        
        ans = float('inf')
        for count, s in l_iter:
            rem = target - s
            set2 = sdict2[n-count]
            i = bisect_left(set2, rem)
            for p in range(i-1, i+1):
                if 0 <= p < len(set2):
                    s1 = s + set2[p]
                    s2 = total - s1
                    ans = min(ans, abs(s1-s2))
        return ans