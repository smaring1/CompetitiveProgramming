class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        flipped = [x[::-1] for x in image]
        for i in range(n):
            for j in range(n):
                flipped[i][j] = abs(flipped[i][j]-1)
        return flipped