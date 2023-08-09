class Solution {

    public void solveSudoku(char[][] board) {
        helper(board,0,0);
    }

    private boolean helper(char grid[][],int i,int j){
        if(i==grid.length){
            return true;
        }
        if(grid[i][j]=='.'){
            for(char k='1';k<='9';k++){
                if(isValid(grid,i,j,k)){
                    grid[i][j]=k;
                    boolean ans = helper(grid,j==8?i+1:i,j==8?0:j+1);
                    if(ans==true) return true;
                    grid[i][j]='.';
                }
            }
            return false;
        }
        else{
            boolean ans = helper(grid,j==8?i+1:i,j==8?0:j+1);
            return ans;
        }
    }

    boolean isValid(char [][]grid,int row,int col,char val){
        for(int j=0;j<9;j++){
            if(grid[row][j]==val || grid[j][col]==val) return false;
        }
        int nr=row/3*3;
        int nc=col/3*3;
        for(int i=nr;i<nr+3;i++){
            for(int j=nc;j<nc+3;j++){
                if(grid[i][j]==val) return false;
            }
        }
        return true;
    }
}