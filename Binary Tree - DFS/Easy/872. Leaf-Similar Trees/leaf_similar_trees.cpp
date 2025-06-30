//Approach - DFS
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaf1, leaf2;
        dfs(root1, leaf1);
        dfs(root2, leaf2);
        return leaf1 == leaf2;
    }

    void dfs(TreeNode* root, vector<int>& leaf) {
        if (!root) return;
        if (!root->left && !root->right) {
            leaf.push_back(root->val);
            return;
        }
        dfs(root->left, leaf);
        dfs(root->right, leaf);
    }
};


//Approach - DFS (Space Optimized)
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaf1;
        dfs(root1, leaf1);
        return dfs1(root2, leaf1) && leaf1.empty();
    }

    void dfs(TreeNode* root, vector<int>& leaf) {
        if (!root) return;
        if (!root->left && !root->right) {
            leaf.push_back(root->val);
            return;
        }
        dfs(root->left, leaf);
        dfs(root->right, leaf);
    }

    bool dfs1(TreeNode* root, vector<int>& leaf) {
        if (!root) return true;
        if (!root->left && !root->right) {
            if (leaf.empty() || leaf.back() != root->val) {
                return false;
            }
            leaf.pop_back();
            return true;
        }
        return dfs1(root->right, leaf) && dfs1(root->left, leaf);
    }
};


//Approach - Iterative DFS
class Solution {
public:
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        stack<TreeNode*> stack1, stack2;
        stack1.push(root1);
        stack2.push(root2);

        while (!stack1.empty() && !stack2.empty()) {
            if (path(stack1) != path(stack2)) {
                return false;
            }
        }
        return stack1.empty() && stack2.empty();
    }
    int path(stack<TreeNode*>& stack) {
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            if (node->right) {
                stack.push(node->right);
            }
            if (node->left) {
                stack.push(node->left);
            }
            if (!node->left && !node->right) {
                return node->val;
            }
        }
        return -1;
    }
};
