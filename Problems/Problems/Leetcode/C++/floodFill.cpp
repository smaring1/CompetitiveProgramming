class Solution {
public:
    int color;
    void fill(vector<vector<int>>& image, int x, int y, int newColor, int m, int n){
        if(x < 0 || y < 0 || x == m || y == n || image[x][y] == newColor || image[x][y] != color) return;
        image[x][y] = newColor;
        fill(image, x+1, y, newColor, m, n);
        fill(image, x, y+1, newColor, m, n);
        fill(image, x-1, y, newColor, m, n);
        fill(image, x, y-1, newColor, m, n);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int m = image.size();
        int n = image[0].size();
        color = image[sr][sc];
        if(color == newColor) return image;
        fill(image, sr, sc, newColor, m, n);
        return image;
    }
};