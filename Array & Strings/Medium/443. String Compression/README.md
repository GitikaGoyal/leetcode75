# 🧩 LeetCode 443: String Compression

> **Problem Link**: [LeetCode - String Compression](https://leetcode.com/problems/string-compression/)  
> **Level**: Medium  
> **Language**: Python 3  

---

## 🧠 Intuition

The task is to compress the input character array in-place by replacing sequences of the same character with the character followed by its count (only if the count > 1).  
This can be efficiently done using two pointers:
- One pointer to **read** (`i`) the input.
- Another to **write** (`idx`) the compressed characters.

---

## 🚀 Approach

1. Initialize:
   - `i` as the reading pointer (start of each group).
   - `idx` as the writing pointer (for in-place overwrite).
   - `n` as the length of `chars`.
2. While `i < n`:
   - Count how many times the current character repeats.
   - Write the character once at position `idx`, then increment `idx`.
   - If count > 1:
     - Convert the count to string and write each digit at `idx`.
3. After processing all characters, return `idx` as the new length of the array.

---

## ⏱️ Complexity

| Metric            | Complexity |
|-------------------|------------|
| Time Complexity   | O(n)       |
| Space Complexity  | O(1)       |

The algorithm only uses a constant amount of extra space and processes the array in a single pass.

---

## 🧑‍💻 Code

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        i, idx, n = 0, 0, len(chars)

        while i < n:
            count = 1
            while (count + i) < n and chars[count + i] == chars[i]:
                count += 1

            chars[idx] = chars[i]
            idx += 1

            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

            i += count

        return idx
