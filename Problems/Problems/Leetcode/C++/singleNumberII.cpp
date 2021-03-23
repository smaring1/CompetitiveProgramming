class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        if (nums.size() <= 3) {
            return 1;
        } else {
            for(int i = 1; i < nums.size()-1; i++) {
                if (nums[i-1] != nums[i] && nums[i-1] != nums[i+1] && i == 1) {
                    return nums[i-1];
                }
                
                if (nums[i+1] != nums[i] && nums[i+1] != nums[i-1] && i == nums.size()-2) {
                    return nums[i+1];
                }
                if (nums[i] != nums[i-1] && nums[i] != nums[i+1]) {
                    return nums[i];
                }
            }
        }
        return 0;
    }
};