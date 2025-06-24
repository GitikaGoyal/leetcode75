class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []

        for i in range(len(asteroids)):
            a = asteroids[i]
            while stack and a < 0 and stack[-1] > 0:
                sum_val = a + stack[-1]
                if sum_val < 0:
                    stack.pop()  # Destroy right side (positive)
                elif sum_val > 0:
                    a = 0        # Destroy current (negative)
                    break
                else:
                    stack.pop()  # Both destroy each other
                    a = 0
                    break

            if a != 0:
                stack.append(a)

        return stack
