def maxProfit(prices):
    max_profit, min_profit = 0, float('inf')
    for price in prices:
        min_profit = min(min_profit, price)
        max_profit = max(price - min_profit, max_profit)
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))