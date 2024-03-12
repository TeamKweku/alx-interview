#!/usr/bin/python3
"""Module that implemets the prime game algorithm"""


def isWinner(x, numbers):
    """Determines the winner of a prime game session with `x` rounds.

    Args:
        x (int): The number of rounds in the game.
        numbers (list): List of integers representing the numbers
        for each round.

    Returns:
        str or None: The winner of the game (either 'Maria' or 'Ben'),
        or None if it's a tie.
    """
    if x < 1 or not numbers:
        return None

    marias_wins, bens_wins = 0, 0

    n = max(numbers)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    for _, n in zip(range(x), numbers):
        primes_count = len(list(filter(lambda x: x, primes[0:n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return "Maria" if marias_wins > bens_wins else "Ben"
