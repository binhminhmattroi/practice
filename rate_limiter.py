5. Rate limiter (design plus code)
Allow at most 3 requests per user in any 10-second window. Write allow(userId, timestamp) returning true or false.

Example for one user: times 1, 2, 3 → allowed; time 4 → denied; time 12 → allowed (the request at time 1 has expired).
Hint: store each user’s recent timestamps in a queue and drop old ones. Discuss what changes with many servers (this touches on distributed systems).

dictionary={}  #key is user and value is queue
def allow(userId,timestamp):
    if userId not in dictionary:
        dictionary[userId] = deque()
        user_queue = dictionary[userId]
        user_queue.append(timestamp)
        return True
    else:
        #find the user queue
        user_queue = dictionary[userId]
        #look through the user queue to clean up
        while user_queue and timestamp-user_queue[0]>=10:
            user_queue.popleft()
        if len(user_queue)<3:
            user_queue.append(timestamp)
            return True
        else:
            return False


The time between the servers have to be in sync?

