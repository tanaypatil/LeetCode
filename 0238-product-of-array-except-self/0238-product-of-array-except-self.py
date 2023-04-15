class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [1], [1]
        
        for num in nums:
            pre.append(num*pre[-1])
            
        for num in nums[::-1]:
            post.append(num*post[-1])
        post.reverse()
        
        result = []
        
        for i in range(len(nums)):
            result.append(pre[i]*post[i+1])
        return result