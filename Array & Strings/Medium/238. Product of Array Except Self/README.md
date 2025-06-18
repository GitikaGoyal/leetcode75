## ✖️ Product of Array Except Self (Two-Pass Approach)

> **LeetCode Problem**  
> 🔗 [Product of Array Except Self – LeetCode](https://leetcode.com/problems/product-of-array-except-self/)  
> 🟠 Difficulty: Medium  
> 🧑‍💻 Language: Python 3

---

## 🧠 Intuition
The challenge is to compute the product of all elements except the current one, without using division and in linear time.
A simple way to think about it is:
For each `i`, the result is the product of all numbers before `i` and all numbers after `i`.

So we break the problem into:
  - Left (prefix) product
  - Right (postfix) product
    
Multiplying both gives the answer for each index.

---

## 🔍 Approach

### 🔁 Two-Pass Method:

1. **Prefix Pass (Left to Right):**
   - Initialize `prefix = 1`.
   - Traverse `nums`, storing `prefix` in `res[i]`, then update `prefix *= nums[i]`.

2. **Postfix Pass (Right to Left):**
   - Initialize `postfix = 1`.
   - Traverse from right to left, multiplying `res[i]` with `postfix`, then update `postfix *= nums[i]`.

3. The result array `res` now contains the product of all elements except the one at each index.

---

## ⏱️ Complexity

| Metric            | Complexity      |
|-------------------|-----------------|
| Time Complexity   | O(n)            |
| Space Complexity  | O(1) (excluding output array) |

---

## 💻 Code

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
