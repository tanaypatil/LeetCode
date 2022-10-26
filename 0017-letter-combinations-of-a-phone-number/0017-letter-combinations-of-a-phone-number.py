from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        num_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        char_list = []
        for d in digits:
            char_list.append(num_map[d])
        p = list(product(*char_list))
        ans = []
        for l in p:
            ans.append(''.join(l))
        return ans