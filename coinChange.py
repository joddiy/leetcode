class Solution(object):
    # dp O(sn) s = |amount|
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_v = amount + 1
        coins = coins[::-1]
        dp = [max_v] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]

    #?
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

            if curCount + (curAmount - 1) / self.coins[i] + 1 >= self.result:
                return

            if curAmount % self.coins[i] == 0:
                self.result = min(self.result, curCount +
                                  curAmount // self.coins[i])
                return

            # try use the biggest coin
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


# Solution().coinChange([186, 419, 83, 408], 6249)
print(Solution().coinChange([1, 2], 2))
