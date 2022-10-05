class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cache = [0] * 26
        for c in tasks:
            cache[ord(c) - ord('A')] += 1
        cache.sort(reverse=True)
        # the last row doesn't need to idle
        max_v = cache[0] - 1
        idle_slots = max_v * n
        for i in range(1, len(cache)):
            if cache[i] == 0:
                break
            idle_slots -= min(cache[i], max_v)
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)


solution = Solution().leastInterval

solution(["A", "A", "A", "B", "B", "B"], 2)
solution(["A", "A", "A", "B", "B", "B"], 0)
solution(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)