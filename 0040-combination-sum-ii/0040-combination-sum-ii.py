def genSum(arr, target_sum, current_sum, index, current_res, res, memo, im):
    im[(current_sum, index, tuple(current_res))] = 1
    if current_sum >= target_sum or index >= len(arr):
        return
    
    if current_sum + arr[index] == target_sum:
        z = tuple(sorted(current_res+[arr[index]]))
        if z not in memo:
            res.append(z)
            memo[z] = 1
        
    if current_sum + arr[index] < target_sum and (current_sum, index+1, tuple(current_res)) not in im:
        # genSum(arr, target_sum, current_sum+arr[index], index, current_res+[arr[index]], res, memo)
        genSum(arr, target_sum, current_sum+arr[index], index+1, current_res+[arr[index]], res, memo, im)
    genSum(arr, target_sum, current_sum, index+1, current_res, res, memo, im)


class Solution:
    def combinationSum2(self, A: List[int], B: int) -> List[List[int]]:
        res = []
        memo = {}
        im = {}
        # A = list(set(A))
        A.sort()
        genSum(A, B, 0, 0, [], res, memo, im)
        return res