class Solution(object):
    # burte force， O(n^2)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(len(height)):
                max_area = max(max_area, (j-i) * min(height[i], height[j]))
        return max_area

    # dp, cannot, since this problem doesn't have optimal sub-strucutre
    # O(n)
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        idx_s, idx_e = 0, len(height)-1
        max_area = 0
        while idx_s < idx_e:
            max_area = max(max_area, min(
                height[idx_s], height[idx_e]) * (idx_e - idx_s))
            # each time, we fasten the shorter height, since only this direction has a better solution
            # area formed between the lines will always be limited by the height of the shorter line
            if height[idx_s] < height[idx_e]:
                idx_s += 1
            else:
                idx_e -= 1
        return max_area


Solution().maxArea([1, 1])
