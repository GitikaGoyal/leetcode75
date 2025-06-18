# 🧩 LeetCode 392: Is Subsequence

> **Problem Link**: [LeetCode - Is Subsequence](https://leetcode.com/problems/is-subsequence/)  
> **Level**: Easy  
> **Language**: Python 3  

---

## 🧠 Intuition

To check whether `s` is a subsequence of `t`, we need to verify if all characters in `s` appear in `t` in the same order, but not necessarily consecutively.  
A natural approach is to use two pointers—one traversing `s` and the other traversing `t`. Whenever we find a matching character, we move the pointer on `s`.

---

## 🚀 Approach

1. Initialize two pointers:
   - `i` for string `s`
   - `j` for string `t`
2. Traverse both strings:
   - If `s[i] == t[j]`, increment both `i` and `j`.
   - Otherwise, increment `j` to keep searching.
3. If all characters in `s` are matched (`i == len(s)`), return `True`.
4. Otherwise, return `False`.

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
