# 🔓 LeetCode 394: Decode String

> **Problem Link**: [LeetCode - Decode String](https://leetcode.com/problems/decode-string/)  
> **Level**: Medium  
> **Language**: C++, Python

---

## 🧠 Intuition

We’re given an encoded string in the format `k[encoded_string]`, where the substring inside `[]` must be repeated `k` times.  
This pattern can be nested — so we must decode from **innermost** to **outermost**, making **stack** the ideal structure for processing characters in a Last-In-First-Out (LIFO) manner.

---

## 🔨 Approach

1. Initialize a stack of strings to simulate processing of characters.
2. Traverse each character in the string `s`:
   - If it’s not `]`, push it onto the stack as a string.
   - If it **is** `]`, do the following:
     - Pop characters from the stack to form the substring until `[` is found.
     - Pop the opening bracket `[`.
     - Then pop digits from the stack to form the repetition count `k`.
     - Repeat the substring `k` times and push the result back onto the stack.
3. Once the entire string has been processed, concatenate all elements in the stack to build the final decoded string.

---

## ⏱️ Complexity

| Metric            | Value        |
|-------------------|--------------|
| Time Complexity   | O(n)         |
| Space Complexity  | O(n)         |
