# 🌿 LeetCode 872: Leaf-Similar Trees

> 📎 **Problem Link**: [LeetCode - Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/)  
> 🟢 **Level**: Easy  
> 🧑‍💻 **Language**: C++

---

## 💡 Intuition

Two binary trees are considered **leaf-similar** if their **leaf value sequence** (from left to right) is the same.  
We need to traverse both trees, collect or compare leaf values, and verify whether both sequences match.

---

## 🧰 Approaches

### 🌲 Approach 1: Recursive DFS

- Traverse both trees using DFS.
- Collect leaf node values in two vectors.
- Compare both vectors for equality.

---

### 🧠 Approach 2: DFS (Space Optimized)

- Traverse the first tree and store leaf values.
- Traverse the second tree and **compare** directly while popping from the first list.
- This avoids creating two full vectors, optimizing space.

---

### 🪜 Approach 3: Iterative DFS (Using Stack)

- Use stacks to simulate DFS for both trees.
- Extract leaf values iteratively and compare them one-by-one.
- Ends early if a mismatch is found.

---

## 📊 Complexity Analysis

| ⚙️ Approach           | ⏱️ Time Complexity | 🗂️ Space Complexity    |
|----------------------|--------------------|------------------------|
| Recursive DFS        | O(n + m)           | O(n + m)               |
| DFS (Space Optimized)| O(n + m)           | O(h₁ + h₂)             |
| Iterative DFS        | O(n + m)           | O(h₁ + h₂)             |

- `n` and `m`: number of nodes in tree1 and tree2.
- `h₁` and `h₂`: heights of tree1 and tree2.
