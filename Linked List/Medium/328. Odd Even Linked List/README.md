# 🔀 LeetCode 328: Odd Even Linked List

> **Problem Link**: [LeetCode - Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

The task is to group all nodes at **odd indices** together followed by nodes at **even indices**, preserving their original relative order.  
This is best done **in-place** using pointer manipulation rather than creating new lists.

---

## 🔨 Approach

### ✅ Approach 1: In-Place Rearrangement (Efficient)

1. If the list is empty or has less than 3 nodes, return head.
2. Use two pointers:
   - `ODD` pointing to the current odd node.
   - `EVEN` pointing to the current even node.
   - Store the head of even nodes using `evenStart`.
3. While `EVEN` and `EVEN->next` exist:
   - Point `ODD->next` to `EVEN->next`.
   - Move `ODD` to the next odd node.
   - Update `EVEN->next` to skip the odd node and go to the next even.
   - Move `EVEN` forward.
4. After loop ends, connect the last odd node to the first even node (`evenStart`).

### ✅ Approach 2: Count-based Rearrangement (Less Common)

1. First, count the total nodes and calculate how many even-positioned nodes are there.
2. Iterate and pull even-positioned nodes and append them at the end.
3. Ensure to nullify the last node’s `next` to avoid cycle.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(1)         |
