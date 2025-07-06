// DFS
// T.C.-> O(n)
// S.C.-> O(n)
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
    int maxLength = 0;
    void zigzagSearch(TreeNode* current, bool moveLeft, int length) {
        if (current == nullptr) {
            return;
        }
        maxLength = max(maxLength, length);
        if (moveLeft) {
            zigzagSearch(current->left, false, length + 1);
            zigzagSearch(current->right, true, 1);
        } else {
            zigzagSearch(current->left, false, 1);
            zigzagSearch(current->right, true, length + 1);
        }
    }
    int longestZigZag(TreeNode* root) {
        zigzagSearch(root, true, 0);
        return maxLength;
    }
};
