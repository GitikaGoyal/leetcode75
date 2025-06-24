# 🔍 LeetCode 1657: Determine if Two Strings Are Close

> **Problem Link**: [LeetCode - Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

To decide if two strings are *close*, we must understand the allowed operations:
1. **Swap any two characters** → allows rearranging characters.
2. **Transform one character into another existing character** → allows frequency swapping but only between already existing characters.

This implies:
- The set of unique characters in both strings must be **identical**.
- The **multiset of character frequencies** must be the same (order doesn’t matter, only counts).

---

## 🔨 Approach

1. **Length Check**: If lengths differ, return `false`.
2. **Count Frequencies**: Use `unordered_map<char, int>` for both strings.
3. **Extract Character Sets & Frequency Vectors**:
   - Collect keys (unique characters) and values (frequencies).
4. **Sort and Compare**:
   - If sorted unique characters differ → `false`.
   - If sorted frequencies differ → `false`.
5. If both checks pass, the strings are close → return `true`.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n log n)   |
| Space Complexity  | O(1) (at most 26 letters) |
