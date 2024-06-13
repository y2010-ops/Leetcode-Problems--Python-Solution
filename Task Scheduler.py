import heapq
import collections as coll
# tasks = ["A","A","A","B","B","C","C"]
# n = 1
tasks = ["A","A","A","B","B","B"]
n = 2
# tasks = ["A","C","A","B","D","B"]
# n = 1
# tasks = ["A","A","A", "B","B","B"]
# n = 3
# tasks = ["A","A","A","B","B","B"]
# n = 50
# tasks = ["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"]
# n = 7
time, h = 0, []
c = coll.Counter(tasks)
for k,v in c.items():
    heapq.heappush(h, (-1)*v)
que = coll.deque()
while len(h) > 0 or que:
    time += 1
    if h:
        remain = heapq.heappop(h)+1
        if remain != 0:
            que.append([remain, n+time])
    else:
        time = que[0][1]

    if que:
        if que[0][1] == time:
            c = que.popleft()[0]
            heapq.heappush(h, c)
