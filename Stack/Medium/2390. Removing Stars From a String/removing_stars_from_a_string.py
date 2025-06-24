#Approach-1 (Using Stack as List)
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)

#Approach-2 (Using Two pointers)
class Solution:
    def removeStars(self, s: str) -> str:
        ch = [''] * len(s)  # Preallocate list
        j = 0

        for i in range(len(s)):
            if s[i] == '*':
                j -= 1
            else:
                ch[j] = s[i]
                j += 1

        return ''.join(ch[:j])
