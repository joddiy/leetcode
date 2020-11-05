from collections import defaultdict
import heapq


def solution(nums, k):
    hash_map = defaultdict(int)
    for num in nums:
        hash_map[num] += 1
    ret = []
    i = 0
    for key, val in hash_map.items():
        if i < k:
            heapq.heappush(ret, (val, key))
        else:
            heapq.heappushpop(ret, (val, key))
        i += 1
    return [v for k, v in ret]


print(solution([1, 1, 1, 2, 2, 3], 2))
print(solution([1], 1))
