class Solution(object):
    # O(m+n)
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums_node = len(nums1) + len(nums2)
        h_1, t_1 = 0, len(nums1)-1
        h_2, t_2 = 0, len(nums2)-1
        while nums_node > 2:
            if t_1 >= 0 and t_2 >= 0:
                if nums1[t_1] > nums2[t_2]:
                    t_1 -= 1
                else:
                    t_2 -= 1
            else:
                if t_1 < 0:
                    t_2 -= 1
                if t_2 < 0:
                    t_1 -= 1
            if h_1 <= len(nums1) - 1 and h_2 <= len(nums2) - 1:
                if nums1[h_1] < nums2[h_2]:
                    h_1 += 1
                else:
                    h_2 += 1
            else:
                if h_1 > len(nums1) - 1:
                    h_2 += 1
                if h_2 > len(nums2) - 1:
                    h_1 += 1
            nums_node -= 2
        if h_1 > t_1:
            return (nums2[h_2] + nums2[t_2])/2.
        if h_2 > t_2:
            return (nums1[h_1] + nums1[t_1])/2.
        return (nums1[h_1] + nums2[t_2])/2.

    # O(log(m+n))
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # divide all elements in {A,B} into two parts with equal length,
        # len(left_part)=len(right_part)
        # max(left_part)≤min(right_part)
        # median = (max(left_part) + min(right_part)) / 2
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return ValueError

        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imax:
            # each loop, take the mid value as i
            i = (imin+imax)//2
            j = half_len - i
            if i < m and nums2[j-1] > nums1[i]:
                # i is too small, must increase it
                imin += 1
            elif i > 0 and nums1[i-1] > nums2[j]:
                # j is too big, must decrease it
                imax -= 1
            else:
                # i is perfect, find the max value of left
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])

                # if odd, left == right, just return left
                if (m + n) % 2 == 1:
                    return max_of_left

                # j is perfect, find the min value of right
                if j == n:
                    min_of_right = nums1[i]
                elif i == m:
                    min_of_right = nums2[j]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right)/2.

# Solution().findMedianSortedArrays([1, 3, 5, 6, 9], [2, 4, 7])
# Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6], [9, 10, 11, 12])
# Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6], [9, 10, 11])
# Solution().findMedianSortedArrays([9, 10, 11], [1, 2, 3, 4, 5, 6])
print(Solution().findMedianSortedArrays([1, 3], [2]))
