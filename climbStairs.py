class Solution(object):
    #case 1
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def recursive(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            return recursive(i+1, n) + recursive(i+2, n)

        return recursive(0, n)

    #case 2
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0 for i in range(n)]

        def recursive(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] > 0:
                return memo[i]
            memo[i] = recursive(i+1, n) + recursive(i+2, n)
            return memo[i]

        return recursive(0, n)

    #case 3
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0] * (n+1)

        memo[0], memo[1] = 1, 1

        if n > 1:
            for i in range(2, n+1):
                memo[i] = memo[i-1] + memo[i-2]

        return memo[n]


print(Solution().climbStairs(5))
