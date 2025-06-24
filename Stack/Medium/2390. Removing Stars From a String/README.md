# ✨ LeetCode 2390: Removing Stars From a String

> **Problem Link**: [LeetCode - Removing Stars From a String](https://leetcode.com/problems/removing-stars-from-a-string/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

Each `*` in the string removes the most recent character before it.  
This pattern resembles a **stack** operation — where:
- Characters are pushed onto the stack.
- On encountering `*`, the most recently added character is **popped**.

---

## 🔨 Approach

1. Initialize an empty `stack<char>`.
2. Traverse the string:
   - If the current character is `*`, pop the top of the stack.
   - Otherwise, push the character onto the stack.
3. Once traversal is complete, the stack will contain all remaining characters in the correct order.
4. Pop each character from the stack and append it to the result string.
5. Reverse the result since stack gives characters in reverse order.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(n)         |
