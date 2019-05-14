class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        candidates = sorted(candidates)
        T = len(candidates)

        def loop(i, cur_sum, solution):
            for i in range(i, T, 1):
                item = candidates[i]
                new_sum = cur_sum+item
                if new_sum < target:
                    loop(i, new_sum, solution + [item])
                elif new_sum > target:
                    return
                else:
                    ret.append(solution + [item])

        loop(0, 0, [])
        return ret


Solution().combinationSum([8,7,4,3], 11)
