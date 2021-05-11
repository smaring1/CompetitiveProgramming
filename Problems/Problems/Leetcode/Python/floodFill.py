class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        def fill(x, y):
            if image[x][y] == color:
                image[x][y] = newColor
                if x >= 1: fill(x-1, y)
                if x+1 < R: fill(x+1, y)
                if y >= 1: fill(x, y-1)
                if y+1 < C: fill(x, y+1)
        color = image[sr][sc]
        if color == newColor: return image
        fill(sr, sc)
        return image