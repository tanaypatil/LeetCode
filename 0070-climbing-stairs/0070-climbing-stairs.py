def numClimbsRec(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return numClimbs(n-1) + numClimbs(n-2)

def numClimbsItr(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    arr = [0]*n
    arr[0], arr[1] = 1, 2
    p = 0
    for i in range(2, n):
        arr[i] = arr[i-1] + arr[i-2]
        p = arr[i]
    return p

class Solution:
    def climbStairs(self, n: int) -> int:
        return numClimbsItr(n)
        