class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def recursion(curr, amount):
            if amount == 0:
                return curr
            min_curr = 1e10
            for coin in coins:
                if coin <= amount:
                    ret_curr = recursion(curr+1, amount-coin)
                    if ret_curr:
                        min_curr = min(min_curr, ret_curr)
            return min_curr

        return recursion(0, amount)

    def coinChange(self, coins, amount):
            """
            :type coins: List[int]
            :type amount: int
            :rtype: int
            """
            coins.sort()
            coins = coins[::-1]
            memo = [0] * (amount+1)

            def recursion(curr, amount):
                if amount == 0:
                    return curr
                if memo[curr] != 0:
                    return memo[curr]
                min_curr = 1e10
                for coin in coins:
                    if coin <= amount:
                        ret_curr = recursion(curr+1, amount-coin)
                        if ret_curr:
                            min_curr = min(min_curr, ret_curr)
                if min_curr != 1e10:
                    memo[amount] = min_curr
                return min_curr
            min_curr = recursion(0, amount)
            if min_curr == 1e10:
                return -1
            else:
                return min_curr

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_v = amount + 1
        dp = [max_v] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        print(dp)
        return -1 if dp[amount] > amount else dp[amount]

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [-1] * (amount+1)
        coins = [coin for coin in coins if coin <= amount]
        if not coins:
            return -1
        min_coin = min(coins)
        for coin in coins:
            dp[coin] = 1
        for i in range(min_coin+1, amount+1):
            min_v = dp[i]
            for coin in coins:
                if i-coin <= 0 or dp[i-coin] == -1:
                    continue
                elif min_v == -1:
                    min_v = dp[i-coin] + 1
                else:
                    min_v = min(dp[i-coin]+1, min_v)
            dp[i] = min_v
        return dp[amount]

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
Solution().coinChange([1, 2], 2)
