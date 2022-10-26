def getSumSet(num, current_sum, path, target_sum, target_len, res):
    if num > 9:
        return
    if current_sum + num == target_sum and len(path) + 1 == target_len:
        res.add(tuple(path+[num]))
    if current_sum + num < target_sum and len(path) + 1 < target_len:
        getSumSet(num+1, current_sum+num, path+[num], target_sum, target_len, res)
    if current_sum < target_sum and len(path) < target_len:
        getSumSet(num+1, current_sum, path, target_sum, target_len, res)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        getSumSet(1, 0, [], n, k, res)
        return res