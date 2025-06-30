# 🌟 LeetCode 1448: Count Good Nodes in Binary Tree

> 📎 **Problem Link**: [LeetCode - Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)  
> 🟠 **Level**: Medium  
> 🧑‍💻 **Language**: C++, Pythpn

---

## 💡 Intuition

A node in a binary tree is called a **good node** if, on the path from the root to that node, there is **no node with a value greater than that node's value**.

To count such nodes, we need to track the **maximum value** seen so far from the root while traversing the tree.

---

## 🧰 Approaches

### 🌲 Approach 1: DFS (Recursive)

- Start from the root node and recursively visit left and right children.
- At each node, keep track of the maximum value seen so far on the path.
- If the current node’s value is greater than or equal to this max value, it’s a good node.

---

### 🪜 Approach 2: BFS (Iterative using Queue)

- Perform level-order traversal (BFS) while storing the max value seen so far along the path.
- At each node, update the max if current node’s value is greater.
- Count nodes that are greater than or equal to the max seen so far.

---

## 📊 Complexity Analysis

| ⚙️ Approach | ⏱️ Time Complexity | 🗂️ Space Complexity |
|------------|--------------------|---------------------|
| DFS        | O(n)               | O(h)                |
| BFS        | O(n)               | O(n)                |

- `n`: Number of nodes in the binary tree.
- `h`: Height of the tree (recursive stack in DFS).
