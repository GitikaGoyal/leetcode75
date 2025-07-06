// BFS
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
private:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if (!root) {
            return ans;
        }
        // Use a queue to perform level order traversal
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            vector<int> level;
            // Process each node in the current level
            for (int i = 0; i < size; i++) {
                TreeNode* top = q.front();
                level.push_back(top->val);
                q.pop();
                // Enqueue the left child if it exists
                if (top->left != NULL) {
                    q.push(top->left);
                }
                // Enqueue the right child if it exists
                if (top->right != NULL) {
                    q.push(top->right);
                }
            }
            // Add the current level to the result
            ans.push_back(level);
        }
        return ans;
    }
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        // Get the level order traversal of the tree
        vector<vector<int>> levelTraversal = levelOrder(root);
        // Iterate through each level and add the last element to the result
        for (auto level : levelTraversal) {
            res.push_back(level.back());
        }
        return res;
    }
};


// DFS
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        recursionRight(root, 0, res);
        return res;
    }
    void recursionRight(TreeNode* root, int level, vector<int> &res){
        if(root == NULL){
            return;
        }
        if(res.size() == level){
            res.push_back(root->val);
        }
        recursionRight(root->right, level + 1, res);
        recursionRight(root->left, level + 1, res);
    }
};
