# 🌲 Maximum Level Sum of a Binary Tree

> 📎 **Problem Link**: [LeetCode - 1161. Maximum Level Sum of a Binary Tree](https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/)  
> 🟠 **Level**: Medium  
> 💻 **Language**: C++, Python

---

## 💡 Intuition

Each level of the binary tree may have a different sum of node values. Our goal is to find the level with the **maximum sum**. Level-order traversal (BFS) naturally suits this, but we can also compute level-wise sums using DFS by maintaining a depth-indexed list.

---

## 🧰 Approach

### 🔹 BFS (Level-Order Traversal)
1. Traverse the tree level by level using a queue.
2. Maintain a `sum` of node values for each level.
3. Update the maximum sum and its level as we go.

### 🔹 DFS (Depth-First Traversal)
1. Use a recursive DFS to go through all nodes.
2. Maintain a `vector<int>` where index = level and value = sum of that level.
3. After traversal, scan through the level sums to find the maximum.

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| BFS      | O(n)            | O(n)             |
| DFS      | O(n)            | O(h) (recursive stack), O(n) for storing sums |
