# 🔍 LeetCode 2215: Find the Difference of Two Arrays

> **Problem Link**: [LeetCode - Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/)  
> **Level**: Easy  
> **Language**: C++, Python  

---

## 🧠 Intuition

We want to find:
- All unique elements in `nums1` **not** present in `nums2`.
- All unique elements in `nums2` **not** present in `nums1`.

Since we're looking for **unique** elements and need **fast lookup**, `unordered_set` (hash set) is ideal.

---

## 🔨 Approach

1. Convert both input vectors into `unordered_set`s:
   - This removes duplicates.
   - Enables constant-time lookups.

2. Iterate over:
   - `set1`, and store elements not in `set2`.
   - `set2`, and store elements not in `set1`.

3. Return a 2D vector of the two result lists.

---

## ⏱️ Complexity

| Metric            | Value     |
|-------------------|-----------|
| Time Complexity   | O(n + m)  |
| Space Complexity  | O(n + m)  |

Where `n` = size of `nums1`, and `m` = size of `nums2`.
