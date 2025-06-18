# 🧩 LeetCode 392: Is Subsequence

> **Problem Link**: [LeetCode - Is Subsequence](https://leetcode.com/problems/is-subsequence/)  
> **Level**: Easy  
> **Language**: Python 3  

---

## 🧠 Intuition

To determine if `s` is a subsequence of `t`, we need to check if all characters in `s` appear in `t` in the same order, though not necessarily consecutively.  
Using two pointers, one for each string, we can scan through `t` and match characters to `s` as we find them.

---

## 🚀 Approach

1. Initialize two pointers:
   - `i` for `s`
   - `j` for `t`
2. Traverse `t` using the `j` pointer:
   - If `s[i] == t[j]`, increment `i` to check the next character in `s`.
   - Always increment `j` to move through `t`.
3. If `i` reaches the length of `s`, it means every character in `s` has been found in order, so return `True`.
4. If the loop ends and `i` is still less than `len(s)`, return `False`.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(1)       |

Where `n` is the length of string `t`.

---

## 🧑‍💻 Code

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
