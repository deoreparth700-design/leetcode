class Solution(object):
   def maxProfit(self, prices):
    lowest_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        profit = prices[i] - lowest_price

        if profit > max_profit:
            max_profit = profit

        if prices[i] < lowest_price:
            lowest_price = prices[i]

    return max_profit