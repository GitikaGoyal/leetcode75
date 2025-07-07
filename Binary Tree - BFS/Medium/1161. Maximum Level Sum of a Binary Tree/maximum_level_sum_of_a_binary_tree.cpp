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
public:
    int maxLevelSum(TreeNode* root) {
        int maxSum= INT_MIN;
        int ans=0;
        int level=0;
        queue<TreeNode*> q;
        q.push(root);
        while(!q.empty())
        {
            level++;
            int sum_currlev=0;
            for(int i=q.size(); i>0; i--)
            {
                TreeNode* node=q.front();
                q.pop();
                sum_currlev+=node->val;

                if(node->left !=nullptr)
                    q.push(node->left);
                if(node->right !=nullptr)
                    q.push(node->right);
            }
            if (maxSum < sum_currlev)
            {
                maxSum = sum_currlev;
                ans=level;
            }
        }
        return ans;
    }
};

//DFS
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
    void dfs(TreeNode* node, int level, vector<int>& sum_currlev)
    {
        if (node == nullptr) {
            return;
        }
        if (sum_currlev.size() == level) {
            sum_currlev.push_back(node->val);
        } else {
            sum_currlev[level] += node->val;
        }

        dfs(node->left, level + 1, sum_currlev);
        dfs(node->right, level + 1, sum_currlev);
    }
    int maxLevelSum(TreeNode* root) {
        vector<int> sum_currlev;
        dfs(root,0, sum_currlev);
        int maxSum= INT_MIN;
        int ans=0;
        for (int i = 0; i < sum_currlev.size(); i++) {
            if (maxSum < sum_currlev[i]) {
                maxSum = sum_currlev[i];
                ans = i + 1;
            }
        }
        return ans;
    }
};
