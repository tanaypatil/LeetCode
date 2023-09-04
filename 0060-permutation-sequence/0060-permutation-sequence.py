class Solution:
    def nextPermutation(self, digits: List[str]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        digits = list(digits)
        pre = digits[:]
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
            
        if i == 0:
            digits[:] = digits[::-1]
            return
        
        j = i
        while j+1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        
        return ''.join(digits)
        
    def factorial(self, n):
        if n == 1:
            return 1
        return n * self.factorial(n-1)
        
    def getPermutation(self, n: int, k: int) -> str:
        s = ""
        for i in range(1, n+1):
            s += str(i)
            
        for i in range(k-1):
            s = self.nextPermutation(s)
            
        return s
            
        
        