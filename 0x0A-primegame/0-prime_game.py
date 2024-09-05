#!/usr/bin/python3
"""This module defines a function that finds the
winner of a prime game based on Sieve of Eratosthenes
"""


def isWinner(x, nums):
    """
    Determines the winner of a game played over x rounds.
    Each round uses numbers from 1 to nums[i], and the winner
    is determined based on the count of prime numbers.

    x: Number of rounds.
    nums: A list where each element represents the upper limit of
          numbers used in each round.

    Returns: The name of the player with the most round wins
             ("Maria" or "Ben"), or None if there's a tie.
    """

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(max_num ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, max_num + 1, p):
                is_prime[multiple] = False

    for n in nums:
        prime_count = sum(is_prime[2:n+1])

        if prime_count % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
