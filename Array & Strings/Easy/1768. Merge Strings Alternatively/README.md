# 🧩 LeetCode 1768: Merge Strings Alternately

> **Problem Link**: [LeetCode - Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)  
> **Level**: Easy  
> **Language**: Python 3  
---

## 🧠 Intuition

The problem is to merge two strings by alternating characters from each string.  
The intuition is straightforward:  
- Take one character from `word1`, then one from `word2`, and continue this process.  
- Once one string is exhausted, append the remaining characters of the longer string.

---

## 🚀 Approach

1. Initialize two pointers `i` and `j` at 0 to iterate through `word1` and `word2`.
2. Use a list `res` to store merged characters (lists are more efficient for string building in Python).
3. While both pointers are within bounds:
   - Append characters alternately from each string.
4. After the loop ends:
   - Append the remaining characters (if any) from `word1` or `word2`.
5. Return the joined string from the result list.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n + m)   |
| Space Complexity  | O(n + m)   |

Where `n` = length of `word1` and `m` = length of `word2`.

---

## 🧑‍💻 Code

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
