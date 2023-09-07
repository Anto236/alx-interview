#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    # Check for invalid input
    if x < 1 or not nums:
        return None

    # Initialize win counters for Maria and Ben
    marias_wins, bens_wins = 0, 0

    # Find the maximum number in the 'nums' list
    n = max(nums)

    # Create a list of boolean values to represent prime numbers up to 'n'
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False  # 1 is not a prime number

    # Use the Sieve of Eratosthenes algorithm
    # to mark non-prime numbers as False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Calculate the number of prime numbers less
    # than or equal to 'n' for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))

        # Update win counters based on whether the
        # count of prime numbers is even or odd
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the overall winner
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
