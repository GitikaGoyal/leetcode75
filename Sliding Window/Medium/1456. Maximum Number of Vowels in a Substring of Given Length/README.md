# 🔤 LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length

> **Problem Link**: [LeetCode - Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)  
> **Level**: Medium  
> **Language**: C++, Python 3  

---

## 🧠 Intuition

We need to find the **maximum number of vowels** in any substring of length `k`.  
This is a classic use-case for the **Sliding Window** technique since:
- The window size is fixed.
- We can efficiently move the window and update the count without recalculating from scratch.

---

## 🔀 Approach: Sliding Window

### ✅ Steps:
1. Create a set of vowels for fast lookup.
2. Calculate the number of vowels in the first `k` characters (initial window).
3. Store this as the current max.
4. Slide the window one character at a time:
   - Add `+1` if the incoming character is a vowel.
   - Subtract `-1` if the outgoing character is a vowel.
   - Update the maximum if the current count is higher.
5. Return the maximum number of vowels seen in any window.

---

### ⏱️ Complexity

| Metric           | Value   |
|------------------|---------|
| Time Complexity  | O(n)    |
| Space Complexity | O(1)    |
