class Solution {


    public static void helper(char[][] grid,boolean[][] vis,int x,int y){

        if(vis[x][y]==true || grid[x][y]=='0'){
            return;
        }

        vis[x][y]=true;

        if(x+1<grid.length && grid[x+1][y]=='1'){
            helper(grid,vis,x+1,y);
        }
        if(y+1<grid[0].length && grid[x][y+1]=='1'){
            helper(grid,vis,x,y+1);
        }
        if(x-1>=0  && grid[x-1][y]=='1'){
            helper(grid,vis,x-1,y);
        }
        if(y-1>=0 && grid[x][y-1]=='1'){
            helper(grid,vis,x,y-1);
        }
    }

    public int numIslands(char[][] grid) {
        int n=grid.length;
        int m=grid[0].length;
        Queue<Character> q=new LinkedList<>();
        boolean[][] vis=new boolean[n][m];
        int c=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(!vis[i][j] && grid[i][j]=='1'){
                    helper(grid,vis,i,j);
                    c++;
                }
            }
        }
        return c;
    }
}
