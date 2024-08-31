#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total) -> int:
    """
    Simple coin algorithms
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to start with the largest denomination
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        num_coins += total // coin
        total %= coin

    # If the total is not zero after trying to use all coins, return -1
    if total != 0:
        return -1

    return num_coins
