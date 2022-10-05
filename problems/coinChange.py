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
                else:
                    break
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

        self.ret = amount + 1

        n = len(coins)
        self.coins = sorted(coins, reverse=True)

        def dfs(cur_amount, cur_count, idx):
            if idx >= n or cur_amount < 0:
                return

            coin = self.coins[idx]
            # if max amount by current coin larger than ret
            if cur_count + cur_amount // coin + (cur_amount % coin !=
                                                 0) >= self.ret:
                return

            # if amount can be divided by current coin
            if cur_amount % coin == 0:
                self.ret = min(self.ret, cur_count + cur_amount // coin)
                return

            # try biggest coin
            dfs(cur_amount - coin, cur_count + 1, idx)

            # try next coin
            dfs(cur_amount, cur_count, idx + 1)

        dfs(amount, 0, 0)
        if self.ret == amount + 1:
            return -1
        else:
            return self.ret


solution = Solution().coinChange
# solution([1, 2, 5], 11)
# solution([2], 3)
# solution([1], 0)
solution([1], 1)