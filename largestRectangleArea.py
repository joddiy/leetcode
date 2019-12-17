class Solution(object):
    
    # O(n^2)
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

    # O(n)
    # we don't need to rescan each item to the left
    # we can reuse results of previous calculations and "jump" through indices in quick manner:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_area = 0
        n = len(heights)
        if n == 0:
            return 0
        left_min, right_min = [0] * n, [0] * n
        left_min[0] = -1
        right_min[n-1] = n
        for i in range(1, n):
            j = i-1
            while j >= 0 and heights[j] >= heights[i]:
                j = left_min[j]
            left_min[i] = j
        for i in range(n-2, -1, -1):
            k = i+1
            while k < n and heights[k] >= heights[i]:
                k = right_min[k]
            right_min[i] = k
        for i in range(n):
            max_area = max(max_area, heights[i]
                           * (right_min[i] - left_min[i]-1))
        return max_area

    # still has queestion about the right boundary
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0) # height[-1] = 0
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # pop the values which are larger than current value
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i) # , but push this value into the stack, because values, 
        heights.pop()
        return ans


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([2]))
print(Solution().largestRectangleArea([]))
print(Solution().largestRectangleArea([2, 3]))
