# 🌲 Longest ZigZag Path in a Binary Tree

> 📎 **Problem Link**: [LeetCode - 1372. Longest ZigZag Path in a Binary Tree](https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/)  
> 🟠 **Level**: Medium  
> 🧑‍💻 **Language**: C++, Python

---

## 💡 Intuition

A ZigZag path in a binary tree alternates between left and right child nodes at every step. The goal is to find the **length of the longest such path** starting from any node.

To solve this, we use **DFS** to traverse the tree and simulate both "left-to-right" and "right-to-left" directions recursively, keeping track of the path length and updating a global maximum.

---

## 🧰 Approach

- Start DFS from the root in both directions (left and right).
- If moving left, recursively call:
  - Left child with direction switched to right (i.e., `moveLeft=False`, `length+1`),
  - Right child with direction kept same but length reset (i.e., `moveLeft=True`, `length=1`).
- If moving right, mirror the logic.
- At each step, update a class-level variable to store the **maximum path length** seen so far.

---

## 📊 Complexity Analysis

| ⚙️ Parameter     | Value         |
|------------------|----------------|
| 🕒 Time Complexity | O(n), where `n` is the number of nodes |
| 🧠 Space Complexity | O(h), where `h` is the height of the tree (worst case O(n) for skewed trees) |
