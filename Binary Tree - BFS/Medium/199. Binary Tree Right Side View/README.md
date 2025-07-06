# 👁️ Binary Tree Right Side View

> 📎 **Problem Link**: [LeetCode - 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)  
> 🟠 **Level**: Medium  
> 💻 **Language**: C++, Python

---

## 💡 Intuition

We want to see the **rightmost node** at each level when viewing a binary tree from the right side. This can be achieved using either **BFS** (level-order traversal) or **DFS** (right-first traversal).

---

## 🧰 Approach

### 🔹 BFS (Level Order Traversal)
1. Traverse the tree level by level using a queue.
2. For each level, capture the **last node** (rightmost).
3. Add it to the result.

### 🔹 DFS (Right-First Recursive Traversal)
1. Traverse the tree with **right-first DFS** to ensure we reach the rightmost node of each level first.
2. Track the current depth (`level`).
3. If it's the first time visiting this depth, add the node to the result.

---

## 📊 Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|----------|-----------------|------------------|
| BFS      | O(n)            | O(n)             |
| DFS      | O(log2 n)            | O(log2 n)|
