# 🌳 Search in a Binary Search Tree

> 📎 **Problem Link**: [LeetCode - 700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)  
> 🟢 **Level**: Easy  
> 💻 **Language**: C++, Python

---

## 💡 Intuition

Binary Search Trees (BSTs) follow a simple rule:
- All nodes in the left subtree are smaller.
- All nodes in the right subtree are greater.

We can leverage this property to efficiently search for a target value, similar to binary search.

---

## 🧰 Approach

### 🔹 Recursive
1. Base case: if the node is `nullptr` or matches the target, return it.
2. If target is less than current node, go to the left subtree.
3. If target is greater, go to the right subtree.

### 🔹 Iterative
1. Use a loop instead of recursion.
2. Traverse the tree by moving left or right based on comparison.
3. Return the matching node or `nullptr` if not found.

---

## 📊 Complexity Analysis

| Approach   | Time Complexity | Space Complexity |
|------------|-----------------|------------------|
| Recursive  | O(h)            | O(h) (recursive stack) |
| Iterative  | O(h)            | O(1)             |

> Here, `h` is the height of the tree, which is `O(log n)` for a balanced tree and `O(n)` for a skewed tree.
