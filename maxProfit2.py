class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        stack = [[0]*3 for i in range(len(prices))]
        stack[0][0] = 0 # rest
        stack[0][1] = -prices[0] # buy
        stack[0][2] = 0 # sell
        bought = stack[0][1]

        for i in range(1, len(prices)):
            stack[i][0] = max(stack[i-1])
            stack[i][1] = stack[i-1][0] - prices[i]
            stack[i][2] = bought + prices[i]
            bought = max(bought, stack[i][1])
        return max(stack[-1])

Solution().maxProfit([1,2,3,0,2])