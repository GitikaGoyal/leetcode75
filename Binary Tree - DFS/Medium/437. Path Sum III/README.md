# 🌟 LeetCode 437: Path Sum III

> 📎 **Problem Link**: [LeetCode - Path Sum III](https://leetcode.com/problems/path-sum-iii/)  
> 🟠 **Level**: Medium  
> 🧑‍💻 **Language**: C++, Python

---

## 💡 Intuition

We are asked to count the number of **paths** in a binary tree where the **sum of the node values** in the path equals a given `targetSum`.

- The path **must move downward** (from parent to child), but **can start and end at any node**.
- This opens the door for **multiple root-to-any-node** and **subtree** based solutions.

---

## 🧰 Approaches

### 🐌 Approach 1: Brute-Force (Recursive DFS)

- For each node, try all paths starting from that node.
- At every node, recursively check if the target sum can be achieved by including the current node and any of its descendants.
- Do this for every node in the tree.

---

### ⚡ Approach 2: Optimized with HashMap (Prefix Sum)

- Use **prefix sum** similar to subarray sum techniques in arrays.
- Maintain a hashmap to store the number of times a prefix sum has occurred.
- For every node, calculate the cumulative sum up to that point and check if `(currSum - targetSum)` exists in the map.
- If yes, it means there exists a path that ends at the current node and adds up to `targetSum`.

---

## 📊 Complexity Analysis

| ⚙️ Approach       | ⏱️ Time Complexity | 🗂️ Space Complexity |
|------------------|--------------------|---------------------|
| Brute-force DFS  | O(n²) (worst-case) | O(h)                |
| Prefix Sum + Map | O(n)               | O(n)                |

- `n`: Number of nodes in the binary tree.
- `h`: Height of the tree (in DFS recursion).
