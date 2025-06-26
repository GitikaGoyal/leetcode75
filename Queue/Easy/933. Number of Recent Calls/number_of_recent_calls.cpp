// Approach-I (Brute-Force using Linear Scan)
// T.C.-> O(n)
// S.C.-> O(total no. of pings)
class RecentCounter {
public:
    vector<int> q;

    RecentCounter() {}

    int ping(int t) {
        q.push_back(t);
        int srange = t - 3000;
        int count = 0;

        for (int time : q) {
            if (time >= srange && time <= t) {
                count++;
            }
        }

        return count;
    }
};

        
// Approach-II (Using Queue)
// T.C.-> O(1)
// S.C.-> O(no. of pings in last 3000ms)
#include <queue>

class RecentCounter {
public:
    queue<int> q;

    RecentCounter() {}

    int ping(int t) {
        q.push(t);
        int srange = t - 3000;

        while (!q.empty() && q.front() < srange) {
            q.pop();
        }

        return q.size();
    }
};
