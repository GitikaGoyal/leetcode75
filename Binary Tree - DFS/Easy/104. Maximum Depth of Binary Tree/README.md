# 🌳 LeetCode 104: Maximum Depth of Binary Tree

> 📎 **Problem Link**: [LeetCode - Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)  
> 🟢 **Level**: Easy  
> 🧑‍💻 **Language**: C++, Python

---

## 🧠 Intuition

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.  
We can solve this problem using various tree traversal strategies such as DFS (recursive and iterative) and BFS.

---

## 🔨 Approach

### ✅ Approach 1: Recursive DFS

- Use post-order traversal (left → right → root).
- At each node, compute the depth of its left and right subtree recursively.
- Return `1 + max(left, right)` for each node.

---

### ✅ Approach 2: Iterative DFS

- Use a stack to simulate the DFS traversal.
- Push `(node, depth)` pairs onto the stack.
- Track the maximum depth encountered while visiting nodes.

---

### ✅ Approach 3: Level Order Traversal (BFS)

- Use a queue to perform level order traversal.
- For each level, increment a counter.
- The final counter value is the maximum depth.

---

## ⏱️ Complexity

| Approach       | Time Complexity | Space Complexity |
|----------------|------------------|-------------------|
| Recursive DFS  | O(n)             | O(h) (height of tree) |
| Iterative DFS  | O(n)             | O(n)              |
| BFS            | O(n)             | O(n)              |
