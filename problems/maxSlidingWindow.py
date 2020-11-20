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
    # O(n) deque, 
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deq = collections.deque([k - 1])  # Store indices
        for i in range(k - 2, -1, -1):
            if nums[i] > nums[deq[0]]:
                deq.appendleft(i)
        
        # deq[0] is current max value
        # deq is a decreased queue
        # every time, we get a new value
        # we compare from the end
        # pop all value which are smaller than this new value
        # insert this new value into the queue
        # so that the queue still is decreased
        ans = [nums[deq[0]]]
        for i in range(k, len(nums)):
            # if current max value is the pop value
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