//Approach-1 (Recursive DFS)
//T.C.-> O(n)
//S.C.-> O(h)
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr)
        return 0;
        return 1 + max(maxDepth(root->left), maxDepth(root->right));   
    }
};

//Approach-2 (Iterative-DFS)
//T.C.->O(n)
//S.C.->O(n)
class Solution {
public:
    int maxDepth(TreeNode* root) {
        stack<pair<TreeNode*, int>> stack;
        stack.push({root, 1});
        int res = 0;

        while (!stack.empty()) {
            pair<TreeNode*, int> current = stack.top();
            stack.pop();
            TreeNode* node = current.first;
            int depth = current.second;

            if (node != nullptr) {
                res = max(res, depth);
                stack.push({node->left, depth + 1});
                stack.push({node->right, depth + 1});
            }
        }
        return res;
    }
};


//Approach-3 (BFS)
//T.C.->O(n)
//S.C.->O(n)
class Solution {
public:
    int maxDepth(TreeNode* root) {
        queue<TreeNode*> q;
        if (root != nullptr) {
            q.push(root);
        }

        int level = 0;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left != nullptr) {
                    q.push(node->left);
                }
                if (node->right != nullptr) {
                    q.push(node->right);
                }
            }
            level++;
        }
        return level; 
    }
};
