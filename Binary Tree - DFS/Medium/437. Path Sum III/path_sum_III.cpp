//Approach: Brute-Force
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
    int pathSum(TreeNode* root, int targetSum) {
        if (root == nullptr)
            return 0;
        return dfs(root, targetSum) +            
           pathSum(root->left, targetSum) +  
           pathSum(root->right, targetSum);
  }
    int dfs(TreeNode* root, long long targetSum) {
        if (root == nullptr)
            return 0;
            // cout << "Visiting node " << root->val << " with targetSum: " << targetSum << endl;
        return (targetSum == root->val) +                
           dfs(root->left, targetSum - root->val) +  
           dfs(root->right, targetSum - root->val);
    }
};



//Approach: Hash Map
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
    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<long long, int> prefixSumCount;
        prefixSumCount[0] = 1;  // Base case: prefix sum = 0 has occurred once
        return dfs(root, 0LL, targetSum, prefixSumCount);
  }

  int dfs(TreeNode* node, long long currSum, int targetSum, unordered_map<long long, int>& prefixSumCount) {
    if (!node)
      return 0;

    currSum += node->val;
    int numPathsToCurr = 0;
        if (prefixSumCount.count(currSum - targetSum)) {
            numPathsToCurr = prefixSumCount[currSum - targetSum];
        }
    prefixSumCount[currSum]++;  // add current sum to map

    int leftPaths = dfs(node->left, currSum, targetSum, prefixSumCount);
    int rightPaths = dfs(node->right, currSum, targetSum, prefixSumCount);

    prefixSumCount[currSum]--;  // backtrack (remove this sum count for other paths)
    
    return numPathsToCurr + leftPaths + rightPaths;
    }
};
