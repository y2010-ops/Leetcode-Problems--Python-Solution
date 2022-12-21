# intervals = [[1,3],[8,10],[2,6],[15,18]]
intervals = [[1, 4], [4, 5]]
interval = sorted(intervals, key = lambda intervals: intervals[0])
i = 1
while i < len(interval):
    if interval[i-1][1]>= interval[i][0]:
        interval[i-1][1] = max(interval[i][1], interval[i-1][1])
        interval.pop(i)
    i += 1
print(interval)