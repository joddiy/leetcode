class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = [[0]*3 for i in range(len(prices))]
        stack[0][0] = 0  # rest
        stack[0][1] = -prices[0]  # buy
        stack[0][2] = 0  # sell
        bought = stack[0][1]

        for i in range(1, len(prices)):
            # for rest, we keep the largest profit from the previous day
            stack[i][0] = max(stack[i-1])
            # for buy, the previous day must rest, [buy, rest, buy] will never happen since rest[i-1] = max(stack[i-1])
            stack[i][1] = stack[i-1][0] - prices[i]
            # for sell, we calculate the profit
            stack[i][2] = bought + prices[i]
            # we record the bought to avoid the [sell, rest, sell], each time we keep the max bought which means the samllest cost bought
            bought = max(bought, stack[i][1])
        return max(stack[-1])


print(Solution().maxProfit([1, 2, 3, 0, 2]))
