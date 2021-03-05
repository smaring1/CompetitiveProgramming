/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    void aux(TreeNode* cur, int n, vector<double>& values, vector<int>& levels) {
        if (!cur) {
            return;
        }
        if (n >= values.size()) {
            values.push_back(cur -> val);
            levels.push_back(1);
        } else {
            values[n] += cur -> val;
            levels[n] += 1;
        }
        aux(cur -> left, n+1, values, levels);
        aux(cur -> right, n+1, values, levels);
        
        
    }
    
    vector<double> averageOfLevels(TreeNode* root) {
        root -> val;
        vector<double> values;
        vector<int> levels;
        aux(root, 0, values, levels);
        for(int i = 0; i < values.size(); i++) {
            values[i] /= levels[i];
        }
        return values;
    }
};