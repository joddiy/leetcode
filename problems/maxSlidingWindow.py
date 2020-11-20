from tools import *
import collections


class Solution(object):
    @print_
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_ = max(nums[0:k])
        ret = [max_]
        for i in range(k, len(nums)):
            if nums[i] >= max_:
                max_ = nums[i]
            elif nums[i - k] != max_:
                pass
            else:
                max_ = max(nums[i + 1 - k:i + 1])
            ret.append(max_)
        return ret

    @print_
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = collections.deque()
        n = len(nums)
        pt = 0
        res = []
        while pt < n:
            # remove all numbers out of range
            while queue and pt - queue[0] > k - 1:
                queue.popleft()
            # maintain descending order in queue
            while queue and nums[queue[-1]] < nums[pt]:
                queue.pop()

            queue.append(pt)
            if pt >= k - 1:
                res.append(nums[queue[0]])
            pt += 1
        return res

    @print_
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Using deque, O(n)
        deq = collections.deque([k - 1])  # Store indices
        for i in range(k - 2, -1, -1):
            if nums[i] > nums[deq[0]]:
                deq.appendleft(i)

        ans = [nums[deq[0]]]
        for i in range(k, len(nums)):
            if deq[0] == i - k:
                deq.popleft()
            while deq and nums[i] >= nums[deq[-1]]:
                deq.pop()

            deq.append(i)
            ans.append(nums[deq[0]])

        return ans


solution = Solution().maxSlidingWindow

solution(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
solution(nums=[1], k=1)
solution(nums=[1, -1], k=1)
solution(nums=[9, 11], k=2)
solution(nums=[4, -2], k=2)