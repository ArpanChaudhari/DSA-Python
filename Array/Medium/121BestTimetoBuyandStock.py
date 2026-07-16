from typing import List


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    buy = prices[0]

    for sell in prices:
        buy = min(buy, sell)
        max_profit = max(max_profit, sell - buy)

    return max_profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))
