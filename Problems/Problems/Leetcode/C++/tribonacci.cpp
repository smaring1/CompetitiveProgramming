class Solution {
public:
    int tribonacci(int n) {
        if (n < 3) {
            if (n == 0) {
                return 0;
            }
            if (n == 1 || n == 2) {
                return 1;
            }
        } else {
            int values[n+1];
            values[0] = 0;
            values[1] = 1;
            values[2] = 1;
            for(int i = 3; i < n+1; i++) {
                values[i] = values[i-1] + values[i-2] + values[i-3];
            }
            return values[n];
        }
        return 0;
    }
};