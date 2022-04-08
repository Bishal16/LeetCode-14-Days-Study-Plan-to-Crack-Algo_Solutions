class Solution:    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # make all node unvisited at first
        r , n = len(grid), len(grid[0])
        visited=[]
        for i in range(r):  
            t=[]
            for j in range(n):
                t.append(0)
            visited.append(t)

        max = 0 # initialize maxirur island area = 0
        for i in range(r):
            for j in range(n):                    
                self.max = 0
                if grid[i][j] == 1 and visited[i][j] == 0: # check only land which is unvisited
                    visited[i][j] = 1
                    self.max += 1
                    
                    def dfs(x,y):
                        # check right node
                        if y < n-1 :
                            if grid[x][y+1] == 1 and visited[x][y+1] == 0:
                                self.max += 1
                                visited[x][y+1] = 1
                                dfs(x, y+1)
                        # check bottom node
                        if x < r-1 :                            
                            if grid[x+1][y] == 1 and visited[x+1][y] == 0:
                                self.max += 1
                                visited[x+1][y] = 1
                                dfs(x+1,y)
                        # check left node
                        if y > 0 :
                            if grid[x][y-1] == 1 and visited[x][y-1] == 0:
                                self.max += 1
                                visited[x][y-1] = 1
                                dfs(x, y-1)
                        # check top node
                        if x > 0 :
                            if grid[x-1][y] == 1 and visited[x-1][y] == 0:
                                self.max += 1
                                visited[x-1][y] = 1
                                dfs(x-1, y)
                        return self.max                                  
                    area = dfs(i,j)
                    if area > max:
                        max = area                    
        return max
                
                
                