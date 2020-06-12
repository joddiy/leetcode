def solution(intervals):
    intervals.sort(key=lambda x: x[0])
    ret = []
    while intervals:
        interval_1 = intervals.pop(0)
        if intervals and interval_1[1] >= intervals[0][0]:
            intervals[0][0] = interval_1[0]
            intervals[0][1] = max(intervals[0][1], interval_1[1])
        else:
            ret.append(interval_1)
    return ret


# print(solution([[2, 6], [1, 3], [8, 10], [15, 18]]))
print(solution([[1, 4], [2, 3]]))
