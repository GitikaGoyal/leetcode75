# 🔍 LeetCode 1207: Unique Number of Occurrences

> **Problem Link**: [LeetCode - Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)  
> **Level**: Easy  
> **Language**: C++, Python3  

---

## 🧠 Intuition

To determine whether all element frequencies in the array are unique:
- First, count how many times each number appears.
- Then, ensure that no two numbers have the same frequency.

If any frequency repeats, we return `False`.

---

## 🔨 Approach

1. Use a `defaultdict` to count the frequency of each number.
2. Use a `set` to store the frequencies we've seen so far.
3. Loop through the frequency values:
   - If the frequency already exists in the set, return `False`.
   - Otherwise, insert the frequency into the set.
4. If no duplicates were found, return `True`.

---

## ⏱️ Complexity

| Metric            | Value     |
|-------------------|-----------|
| Time Complexity   | O(n)      |
| Space Complexity  | O(n)      |

Where `n` is the length of the input array `arr`.
