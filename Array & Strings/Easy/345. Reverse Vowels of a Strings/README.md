# 🔁 Reverse Vowels of a String

> **LeetCode Problem**  
> 🔗 [Reverse Vowels of a String – LeetCode](https://leetcode.com/problems/reverse-vowels-of-a-string/)  
> 🟢 Difficulty: Easy  
> 🧑‍💻 Language: Python 3

---

## 🧠 Intuition

The goal is to reverse only the vowels in a given string, while keeping the other characters in place.  
A natural approach is to use the **two-pointer technique**: scan the string from both ends, and swap vowels when found.

---

## 🔍 Approach

1. Define a set of vowels (both lowercase and uppercase).
2. Convert the string to a list (`new_s`) to allow in-place modification.
3. Initialize two pointers:
   - `i` from the start (0),
   - `j` from the end (`len(s) - 1`).
4. Move `i` forward until a vowel is found.
5. Move `j` backward until a vowel is found.
6. Swap `new_s[i]` and `new_s[j]`.
7. Repeat steps 4–6 until `i >= j`.
8. Join and return the updated list as a string.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(n)       |

---

## 💻 Code

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = ['a','e','i','o','u','A','E','I','O','U']
        new_s = list(s)
        i, j = 0, len(s) - 1
        while i <= j:
            while i < j and s[i] not in vow:
                i += 1
            while i < j and s[j] not in vow:
                j -= 1
            new_s[i], new_s[j] = new_s[j], new_s[i]
            i += 1
            j -= 1
        return ''.join(new_s)
