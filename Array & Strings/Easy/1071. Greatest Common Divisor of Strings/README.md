# 🧩 LeetCode 1071: GCD of Strings

> **Problem Link**: [LeetCode - GCD of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)  
> **Level**: Easy  
> **Language**: C++, Python

---

## 🧠 Intuition

The goal is to find the largest string `X` such that both `str1` and `str2` can be formed by repeating `X` one or more times.  
This is conceptually similar to finding the greatest common divisor (GCD) in arithmetic — but for strings.

Key insights:
- If such a string `X` exists, it must divide the lengths of both input strings.
- Repeating this string the appropriate number of times should reconstruct both `str1` and `str2`.

---

## 🚀 Approach

1. Calculate the lengths of `str1` and `str2` as `len1` and `len2`.
2. Define a helper function `isDivisor(l)` that:
   - Checks if `l` divides both `len1` and `len2`.
   - Validates that repeating the prefix `str1[:l]` reconstructs both strings.
3. Loop from `min(len1, len2)` down to `1`:
   - For each `l`, check if it is a valid divisor using `isDivisor(l)`.
   - Return the first valid substring (largest possible due to descending order).
4. If no valid divisor is found, return an empty string.

---

## ⏱️ Complexity

| Metric            | Complexity                    |
|-------------------|-------------------------------|
| Time Complexity   | O((n + m) × min(n, m))        |
| Space Complexity  | O(n + m)                      |

Where `n = len(str1)` and `m = len(str2)`.

---

## 🧑‍💻 Code

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            factor1, factor2 = len1 // l, len2 // l
            return str1[:l] * factor1 == str1 and str1[:l] * factor2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]
        return ""
