#!/usr/bin/python3
"""
A module that solves the making change popular interview question
using the greedy algorithm
"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the given
    total amount using the greedy algorithm.

    Args:
        coins (list[int]): A list of coin denominations.
        total (int): The target total amount.

    Returns:
        int: Fewest number of coins needed to meet the total.
            If total is 0 or less, returns 0.
            If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0
    remainder = total
    coins_count = 0
    coin_idx = 0
    # sorting list of coin change in descending order
    sorted_coins = sorted(coins, reverse=True)

    n = len(coins)
    while remainder > 0:
        if coin_idx >= n:
            return -1
        if remainder - sorted_coins[coin_idx] >= 0:
            remainder -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
