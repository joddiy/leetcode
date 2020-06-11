class Solution(object):
    # case 1
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     max_so_far = 0
    #     max_ending_here = 0
    #     for i in range(1, len(prices)):
    #         item = prices[i] - prices[i-1]
    #         max_ending_here += item
    #         if max_ending_here < 0:
    #             max_ending_here = 0
    #         elif max_so_far < max_ending_here:
    #             max_so_far = max_ending_here
    #     return max_so_far
    # case 2
    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     if len(prices) < 2:
    #         return 0
    #     item_0 = prices[1] - prices[0]
    #     max_so_far, curr_max = item_0, item_0
    #     for i in range(2, len(prices)):
    #         item = prices[i] - prices[i-1]
    #         curr_max = max(item, curr_max+item)
    #         max_so_far = max(max_so_far, curr_max)
    #     if max_so_far < 0:
    #         return 0
    #     return max_so_far

    # case 3
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        lowest = prices[0]
        rst = 0
        for price in prices:
            if price < lowest:
                lowest = price
            rst = max(rst, price-lowest)
        return rst


print(Solution().maxProfit([7, 6, 4, 3, 1]))
