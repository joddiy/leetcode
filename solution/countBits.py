class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        f = [0]
        for i in range(1, num):
            f.append(f[i // 2] + i % 2)
        return f


print(Solution().countBits(5))
