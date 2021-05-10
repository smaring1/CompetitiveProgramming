class Solution {
public:
    int binarySearch(vector<int>& arr, int l, int r, int x) {
        if (r >= l) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == x)
                return mid;
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);
            return binarySearch(arr, mid + 1, r, x);
        }
        return -1;
    }
    
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(int i = 0; i < matrix.size(); i++) {
            if (!(target > matrix[i][matrix[i].size()-1])) {
                int a = binarySearch(matrix[i], 0, matrix[i].size()-1, target);
                return a != -1;
            }
        }
        return false;
    }
};