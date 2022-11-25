class Solution(object):
    def maxprofit(self, prices):
        """
        https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        :type prices: List[int]
        :rtype: int

        Algorithm:
        Use two index pointers called "left" and "right" initialized as the first and second index positions of our
        prices list. Also initialize a variable called "max_profit" with a starting value of 0.
        Loop through the list from list[right] to list[len(list)], and at each iteration, calculate the possible
        profit: prices[right] - prices[left]. If this value is positive, update the maximum_profit value to the bigger
        value between itself or the new positive profit value.
        """
        left = 0  # Buy
        right = 1  # Sell
        max_profit = 0
        while right < len(prices):
            possible_profit = prices[right] - prices[left]
            if possible_profit > 0:
                max_profit = max(possible_profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit


a = Solution()
prices = [7, 1, 5, 3, 6, 4]
b = a.maxprofit(prices)
print(b)  # should print 5
