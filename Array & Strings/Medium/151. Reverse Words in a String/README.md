# 🔄 Reverse Words in a String

> **LeetCode Problem**  
> 🔗 [Reverse Words in a String – LeetCode](https://leetcode.com/problems/reverse-words-in-a-string/)  
> 🟢 Difficulty: Easy  
> 🧑‍💻 Language: Python 3

---

## 🧠 Intuition

We are asked to reverse the **order of words** in a string.  
The words are separated by spaces, and the output must:

- Have words in **reverse order**.
- Contain exactly **one space** between words.
- Have **no leading or trailing spaces**.

---

## 🔍 Approach

1. Use `split()` to break the input string into a list of words. This automatically removes extra whitespace.
2. Use `reversed()` to reverse the list of words.
3. Use `' '.join()` to combine them back into a single string with exactly one space between words.
4. Return the final reversed string.

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
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_words = reversed(words)
        reversed_sentence = ' '.join(reversed_words)
        return reversed_sentence
