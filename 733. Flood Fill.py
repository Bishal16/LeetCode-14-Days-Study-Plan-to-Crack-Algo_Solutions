class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        r, c = len(image), len(image[0]) 
        
        visited =[]
        for i in range(r):
            visited.append([0]*c)
        
        def FloodFill(x,y):
            if image[x][y] == oldColor and visited[x][y] == 0:
                image[x][y] = newColor
                visited[x][y] = 1                               
                if x>0:
                    FloodFill(x-1, y)   #top node                
                if y<c-1:
                    FloodFill(x, y+1)   #right node                
                if x<r-1:
                    FloodFill(x+1, y)   #bottom node               
                if y>0:
                    FloodFill(x, y-1)   #left node                
        FloodFill(sr,sc)
        return image