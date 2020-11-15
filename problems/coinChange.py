from tools import *


class Solution(object):
    @print_
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0

        coins.sort()
        dp = [amount + 1] * (amount + 1)  # min coins number for amount i
        for i in range(1, amount + 1):
            for c in coins:
                if i == c:
                    dp[i] = 1
                elif i - c > 0 and dp[i - c] > 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[-1] > amount else dp[-1]

    @print_
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if len(coins) == 0:
            return -1
        if amount == 0:
            return 0

        self.coins = sorted(set(coins), reverse=True)

        def helper(curAmount, curCount, i):
            # result is larger than min, continue
            if curCount + (curAmount - 1) / self.coins[i] + 1 >= self.result:
                return
            # current amount can be divided coins, update
            if curAmount % self.coins[i] == 0:
                self.result = min(self.result,
                                  curCount + curAmount // self.coins[i])
                return

            # try use the biggest coin first
            if curAmount > self.coins[i]:
                helper(curAmount - self.coins[i], curCount + 1, i)
            # else try not to use the biggest coin
            if i < len(self.coins) - 1:
                helper(curAmount, curCount, i + 1)

        self.result = amount + 1
        helper(amount, 0, 0)
        if self.result == amount + 1:
            return -1
        else:
            return self.result


solution = Solution().coinChange
solution([1, 2, 5], 11)
solution([2], 3)
solution([1], 0)