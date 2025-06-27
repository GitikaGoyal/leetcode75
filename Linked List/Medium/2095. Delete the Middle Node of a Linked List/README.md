# 🧹 LeetCode 2095: Delete the Middle Node of a Linked List

> **Problem Link**: [LeetCode - Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

To delete the **middle node** of a singly-linked list, we can use the **slow and fast pointer** technique:
- The **slow** pointer moves one step at a time.
- The **fast** pointer moves two steps at a time.
- When the fast pointer reaches the end, the slow pointer is at the middle.

To delete the middle node, we also need to keep track of the node **before** the slow pointer.

---

## 🔨 Approach

1. Initialize:
   - `slow` and `fast` pointers at `head`.
   - `prevSlow` as `nullptr` to track the node before `slow`.
2. Traverse the list:
   - Move `fast` two steps and `slow` one step until `fast` reaches the end.
   - `prevSlow` tracks the node before the middle.
3. If the list has only one node (`prevSlow == nullptr`), return `nullptr`.
4. Else, delete the `slow` node (middle), by setting `prevSlow->next = slow->next`.
5. Return the modified head.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(1)         |
