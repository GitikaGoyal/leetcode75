# 🔍 Lowest Common Ancestor of a Binary Tree

> 📎 **Problem Link**: [LeetCode - 236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)  
> 🟠 **Level**: Medium  
> 💻 **Language**: C++, Python

---

## 💡 Intuition

To find the **lowest common ancestor (LCA)** of two nodes `p` and `q` in a binary tree, we need to identify the lowest node in the tree that has both `p` and `q` as descendants.

The key idea is to use **post-order DFS** traversal:
- Traverse the left and right subtrees.
- If both subtrees return non-null, the current node is the LCA.
- If only one side returns non-null, propagate that up (it means only one of `p` or `q` was found so far).

---

## 🧰 Approach

1. Perform DFS starting from the root.
2. If the current node is `null`, `p`, or `q`, return it.
3. Recursively search left and right subtrees.
4. Based on results:
   - If both left and right return non-null, current node is the LCA.
   - If only one is non-null, return that node upward.

---

## 📊 Complexity Analysis

| ⚙️ Parameter     | Value         |
|------------------|----------------|
| 🕒 Time Complexity | O(n), where `n` is the number of nodes in the tree |
| 🧠 Space Complexity | O(h), where `h` is the height of the tree (O(n) worst case for skewed tree) |
