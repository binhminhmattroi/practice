5. Rate limiter (design plus code)
Allow at most 3 requests per user in any 10-second window. Write allow(userId, timestamp) returning true or false.

Example for one user: times 1, 2, 3 → allowed; time 4 → denied; time 12 → allowed (the request at time 1 has expired).
Hint: store each user’s recent timestamps in a queue and drop old ones. Discuss what changes with many servers (this touches on distributed systems).
