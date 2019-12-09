class Solution(object):
    # Time Limit Exceeded
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(heights)
        for i in range(n):
            j, k = i-1, i+1
            while j >= 0 and heights[j] >= heights[i]:
                j -= 1
            while k < n and heights[k] >= heights[i]:
                k += 1
            max_area = max(max_area, (k-j-1) * heights[i])
        return max_area

    # corrent idea but cannot run
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights = [0]+heights+[0]
        n = len(heights)
        left_min = [0] * n
        max_area = 0
        k = 0
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                left_min[i] = i
            elif heights[i] < heights[i-1]:
                left_min[i] = i-k
                k = -1
            else:
                left_min[i] = left_min[i-1]
            k += 1
        print(left_min)
        right_min = [n-1] * n
        k = 0
        for i in range(n-2, -1, -1):
            if heights[i] > heights[i+1]:
                right_min[i] = i
            elif heights[i] < heights[i+1]:
                right_min[i] = i+k-1
                k = -1
            else:
                right_min[i] = right_min[i+1]
            k += 1
        print(right_min)
        for i in range(n):
            max_area = max(max_area, heights[i]
                           * (right_min[n-1-i]-left_min[i]))
        return max_area

    #
    # def largestRectangleArea(self, heights):
    #     """
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     heights.append(0)
    #     stack = [-1]
    #     ans = 0
    #     for i in range(len(heights)):
    #         while heights[i] < heights[stack[-1]]:
    #             h = heights[stack.pop()]
    #             w = i - stack[-1] - 1
    #             ans = max(ans, h * w)
    #         stack.append(i)
    #     heights.pop()
    #     return ans


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(Solution().largestRectangleArea([2]))
# print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2, 3]))
