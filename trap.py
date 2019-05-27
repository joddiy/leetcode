class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        dp_l, dp_r = [0] * len(height), [0] * len(height)
        dp_l[0] = height[0]
        dp_r[-1] = height[-1]
        ret = 0
        for i in range(1, len(height)):
            dp_l[i] = max(dp_l[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            dp_r[i] = max(dp_r[i+1], height[i])
        for i in range(1, len(height)):
            ret += min(dp_l[i], dp_r[i]) - height[i]
        return ret



Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
