#Approach-I (Brute-Force using Linear Scan)
#T.C.-> O(n)
#S.C.-> O(total no. of pings)
class RecentCounter:
    def __init__(self):
        self.q = list()
    def ping(self, t: int) -> int:
        if t is None:
            return None
        else:
            self.q.append(t)
            srange = t-3000
            erange = t
            count = 0
            for i in self.q:
                if i>=srange and i<=erange:
                    count+=1
            return count
        
#Approach-II (Using Queue)
#T.C.-> O(1)
#S.C.-> O(no. of pings in last 3000ms)
from collections import deque
class RecentCounter:

    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        self.q.append(t)
        srange = t-3000
        erange = t
        count = 0
        while self.q[0]<srange:
            self.q.popleft()
        return len(self.q)
    
