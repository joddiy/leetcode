def solution(nums):
    slow = nums[0]
    fast = nums[nums[0]]
    while fast != slow:
        fast = nums[nums[fast]]
        slow = nums[slow]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


print(solution([1, 3, 4, 2, 2]))
