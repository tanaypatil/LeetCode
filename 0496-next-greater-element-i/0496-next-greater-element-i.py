from collections import deque


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = deque()
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[0] <= nums2[i]:
                stack.popleft()
            if not stack:
                nextGreater[nums2[i]] = -1
            else:
                nextGreater[nums2[i]] = stack[0]
            stack.appendleft(nums2[i])
        ret = []
        for i, a in enumerate(nums1):
            ret.append(nextGreater[a])
        return ret
        