A queue is first-in, first-out: items leave in the order they arrived. In Python, use collections.deque. popleft() removes from the front in O(1). A list’s pop(0) is O(n), because every other item shifts over by one.

python
from collections import deque
q = deque()
q.append(5)       # add to the back
q.append(8)
q.popleft()       # removes 5, the oldest
q[0]              # peek at the front: 8

Rate limiter: Write a class RateLimiter that allows at most 3 requests per 10 seconds. The method allow(t) takes the time t in seconds and returns True if the request is allowed, or False if it is blocked. Times arrive in increasing order. A request at time t counts the requests in the window from t - 9 to t, inclusive.

Example:

allow(1) → True (1 request in the window)
allow(2) → True (2 requests)
allow(5) → True (3 requests)
allow(8) → False (already 3 requests in 1 to 8)
allow(11) → True (the request at 1 is now outside the window 2..11, so there are 2 left, and this one makes 3)

Blocked requests are not recorded.

Before you code it, answer this: what should the queue hold, and what do you do at the front of the queue when a new request arrives? Then write the class and paste it.

the queue holds t in seconds, the front would be the oldest of the 3 requests
class RateLimiter():
    def __init__(self):
        self.d=deque()
    
    def allow(self, t):
        #diff_time = t-oldest_time
        #look through the queue and clean up first?
        #for i,_ in enumerate(self.d):
        #    if(t-self.d[i]>10):
        while self.d and t - self.d[0] >= 10:
            self.d.popleft()
        if len(self.d) < 3:
            self.d.append(t)
            return True
        else:
            return False
