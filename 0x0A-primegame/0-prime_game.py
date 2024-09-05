#!/usr/bin/python3
"""
Winner of a game
"""


def isWinner(x, nums):
    """
    Who is the winner
    """
    if not nums or x < 1:
        return None

    def sieve(n):
        # Sieve of Eratosthenes to find all primes up to n
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return sieve

    # Find the largest number in nums to perform sieve only once
    max_num = max(nums)
    prime = sieve(max_num)

    # Prime count up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Maria wins if the count of primes up to n is odd
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
