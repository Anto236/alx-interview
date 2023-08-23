#!/usr/bin/python3
"""function determine the fewest number of coins
   needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    :param coins: List of coin values in your possession
    :param total: Amount total to be met
    :return: Fewest number of coins needed to meet total
             If total is 0 or less, return 0
             If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    """Initialize a list to store the minimum
       number of coins needed for each value from 1 to total
    """
    min_coins = [float('inf')] * (total + 1)
    """Base case: 0 coins are needed to make a total of 0"""
    min_coins[0] = 0
    """Iterate through each coin value and update the min_coins list"""
    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    """If min_coins[total] is still infinity,
       it means the total cannot be made using the given coins
    """
    if min_coins[total] == float('inf'):
        return -1
    return min_coins[total]
