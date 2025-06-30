# 🔗 LeetCode 2130: Maximum Twin Sum of a Linked List

> **Problem Link**: [LeetCode - Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

In a linked list of even length, a twin sum is defined as the sum of the ith node from the start and the ith node from the end.  
To solve this problem, we need to compute the maximum of these twin sums.

---

## 🔨 Approach

### ✅ Approach 1: Using Array (Brute Force)

1. Traverse the entire linked list and store all values in an array.
2. Use two pointers to compute twin sums from both ends of the array.
3. Track the maximum twin sum.

---

### ✅ Approach 2: Using Stack

1. Traverse the entire list and push all values onto a stack.
2. Traverse only the first half of the list.
3. At each step, pop a value from the stack and compute the twin sum.
4. Track the maximum twin sum.

---

### ✅ Approach 3: Reverse Second Half (Optimal)

1. Use the slow and fast pointer approach to find the middle of the list.
2. Reverse the second half of the list.
3. Traverse the first and reversed second half simultaneously to compute twin sums.
4. Return the maximum.

---

## ⏱️ Complexity

| Approach         | Time Complexity | Space Complexity |
|------------------|------------------|-------------------|
| Array            | O(n)             | O(n)              |
| Stack            | O(n)             | O(n)              |
| Reverse Half     | O(n)             | O(1)              |
