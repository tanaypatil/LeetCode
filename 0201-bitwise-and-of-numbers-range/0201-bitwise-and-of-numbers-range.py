class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            i += 1
            left >>= 1
            right >>= 1
        return left << i
        