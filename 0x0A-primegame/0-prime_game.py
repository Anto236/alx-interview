#!/usr/bin/python3
"""Prime Game"""


def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determine the winner of each game round.

    Args:
        x (int): The number of rounds.
        nums (list): An array of integers representing
        the range of numbers for each round.

    Returns:
        str or None: The name of the player that won
        the most rounds. If the winner cannot be determined, returns None.
    """
    if x <= 0 or not nums:
        return None

    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))
        if prime_count % 2 == 0:
            wins["Ben"] += 1
        else:
            wins["Maria"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Maria"] < wins["Ben"]:
        return "Ben"
    else:
        return None
