class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        tmp_ret = [0] * len(T)
        temp_range = {i: [] for i in range(30, 101)}
        for id, temp in enumerate(T):
            temp_range[temp].append(id)
            for i in range(30, temp):
                while len(temp_range[i]) != 0:
                    tmp_item = temp_range[i].pop()
                    tmp_ret[tmp_item] = id - tmp_item
        return tmp_ret

    def dailyTemperatures2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
