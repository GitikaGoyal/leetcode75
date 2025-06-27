#Approach-I(Brute-Force)
#T.C.->O(n^2)
#S.C.->O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        while True:
            i = 0
            while i < len(s):
                if 'R' not in s:
                    return "Dire"
                if 'D' not in s:
                    return "Radiant"
                if s[i] == 'R':
                    j = (i + 1) % len(s)
                    while s[j] == 'R':
                        j = (j + 1) % len(s)
                    s.pop(j)
                    if j < i:
                        i -= 1
                else:
                    j = (i + 1) % len(s)
                    while s[j] == 'D':
                        j = (j + 1) % len(s)
                    s.pop(j)
                    if j < i:
                        i -= 1
                i += 1

#Approach-II (Greedy-Two Queues)
#T.C.->O(n)
#S.C.->O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        D, R = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == 'R':
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if rTurn < dTurn:
                R.append(rTurn + n)
            else:
                D.append(dTurn + n)

        return "Radiant" if R else "Dire"

#Approach-III (Greedy)
#T.C.->O(n)
#S.C.->O(n)
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        cnt = i = 0

        while i < len(senate):
            c = senate[i]
            if c == 'R':
                if cnt < 0:
                    senate.append('D')
                cnt += 1
            else:
                if cnt > 0:
                    senate.append('R')
                cnt -= 1
            i += 1
        
        return "Radiant" if cnt > 0 else "Dire"
