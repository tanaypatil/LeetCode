class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = [0]*n
        for index, num in enumerate(nums2):
            pos[num] = index
            
        pos_b = [pos[nums1[0]]]
        pre_a = [0] # i: number of common elements before nums1[i] in both nums1 and nums2
        
        for a in nums1[1:]:
            index = pos[a]
            pindex = bisect_right(pos_b, index)
            pos_b.insert(pindex, index)
            pre_a.append(pindex)
        
        pos_b = [pos[nums1[-1]]]
        suf_a = [0] # i: number of common elements after nums1[i] in both nums1 and nums2
        
        for a in nums1[n-2::-1]:
            index = bisect_right(pos_b, pos[a])
            suf_a.append(len(pos_b)-index)
            pos_b.insert(index, pos[a])
        
        suf_a.reverse()
        ans = 0
        for pre, suf in zip(pre_a, suf_a):
            ans += pre * suf
        return ans
        