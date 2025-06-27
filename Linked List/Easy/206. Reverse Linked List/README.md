# 🔁 LeetCode 206: Reverse Linked List

> **Problem Link**: [LeetCode - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  
> **Level**: Easy  
> **Language**: C++, Python

---

## 🧠 Intuition

Reversing a singly linked list involves changing the direction of each node's `next` pointer so that the list points in the opposite direction.  
This can be done either recursively (using call stack) or iteratively (using three pointers).

---

## 🔨 Approach

### ✅ Approach 1: Recursion

- Base case: if the list is empty or has only one node, return it.
- Recurse on the `next` node.
- Once recursion returns, set `head->next->next = head` to reverse the link.
- Set `head->next = nullptr` to avoid cycle.
- Return the new head (last node of original list).

### ✅ Approach 2: Iteration (Three Pointers)

- Initialize three pointers: `prev = nullptr`, `curr = head`, `next = nullptr`.
- Traverse the list while `curr` is not null:
  - Temporarily store `curr->next`.
  - Point `curr->next` to `prev`.
  - Move `prev` and `curr` forward.
- Return `prev` as the new head.

---

## ⏱️ Complexity

| Metric            | Recursive     | Iterative     |
|-------------------|---------------|---------------|
| Time Complexity   | O(n)          | O(n)          |
| Space Complexity  | O(n) (stack)  | O(1)          |
