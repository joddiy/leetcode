from collections import defaultdict

def solution(strs):
    ret = defaultdict(list)
    for s in strs:
        ret[tuple(sorted(s))].append(s)
    return list(ret.values())

# print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution(["cab","pug","pei","nay","ron","rae","ems","ida","mes"]))
