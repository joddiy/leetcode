# O(klogk+2(n-k)logk)
def solution(nums, k):
    import heapq
    k_heap = nums[0:k]
    heapq.heapify(k_heap)
    for i in range(k, len(nums)):
        heapq.heappush(k_heap, nums[i])
        heapq.heappop(k_heap)
    return heapq.heappop(k_heap)


# O(n)
def solution(nums, k):

    def recursive(nums, k):
        pivot = nums.pop(len(nums) // 2)
        right = [num for num in nums if num > pivot]
        lr = len(right)
        if k == lr + 1:
            return pivot
        elif k < lr + 1:
            return recursive(right, k)
        else:
            left = [num for num in nums if num <= pivot]
            return recursive(left, k - lr - 1)

    return recursive(nums, k)


print(solution([3, 2, 1, 5, 6, 4], 2))
print(solution([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
