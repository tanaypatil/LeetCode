def genSum(arr, target_sum, current_sum, index, current_res, res, memo):
    if current_sum > target_sum or index >= len(arr):
        return
    
    if current_sum + arr[index] == target_sum:
        z = tuple(sorted(current_res+[arr[index]]))
        if z not in memo:
            res.append(z)
            memo[z] = 1
        
    if current_sum + arr[index] < target_sum:
        genSum(arr, target_sum, current_sum+arr[index], index, current_res+[arr[index]], res, memo)
        genSum(arr, target_sum, current_sum+arr[index], index+1, current_res+[arr[index]], res, memo)
    genSum(arr, target_sum, current_sum, index+1, current_res, res, memo)


class Solution:
    def combinationSum(self, A: List[int], B: int) -> List[List[int]]:
        res = []
        memo = {}
        A = list(set(A))
        A.sort()
        genSum(A, B, 0, 0, [], res, memo)
        return res