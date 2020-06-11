class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = [0] * 26
        for char in tasks:
            map[ord(char) - ord('A')] += 1
        map.sort()
        time = 0
        while map[25] > 0:
            i = 0
            while i <= n:
                if map[25] == 0:
                    break
                if i < 26 and map[25-i] > 0:
                    map[25-i] -= 1
                i += 1
                time += 1
            map.sort()
        return time

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import heapq

        map = [0] * 26
        for char in tasks:
            map[ord(char) - ord('A')] -= 1
        queue = []
        heapq.heapify(queue)
        for f in map:
            if f < 0:
                heapq.heappush(queue, f)
        time = 0
        while len(queue) != 0:
            i = 0
            tmp = []
            while i <= n:
                if len(queue) != 0:
                    if heapq.nsmallest(1, queue)[0] < -1:
                        tmp.append(heapq.heappop(queue)+1)
                    else:
                        heapq.heappop(queue)
                time += 1
                if len(queue) == 0 and len(tmp) == 0:
                    break
                i += 1
            for l in tmp:
                heapq.heappush(queue, l)
        return time

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        map = [0] * 26
        for char in tasks:
            map[ord(char) - ord('A')] += 1
        map.sort()
        max_val = map[25] - 1
        idle_slots = max_val * n
        for i in range(24, -1, -1):
            if map[i] <= 0:
                break
            idle_slots -= min(map[i], max_val)
        return idle_slots+len(tasks) if idle_slots > 0 else len(tasks)

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = [0]*26
        for task in tasks:
            cnt[ord(task)-65] += 1
        s = list(sorted(cnt))
        i = 25
        mx = s[-1]
        m = len(tasks)
        while i >= 0 and s[i] == mx:
            i -= 1
        return max(m, (mx-1)*(n+1)+25-i)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
