class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        mat = [[1], [1, 1]]
        
        if numRows == 1:
            return[[1]]
        if numRows == 2:
            return mat
        
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(mat[i-1][j-1] + mat[i-1][j])
            temp.append(1)
            mat.append(temp)
        return mat
        