def fatorial(n):
    """
    Calculates the factorial of a number using recursion.

    Args:
        n (int): Positive integer.

    Returns:
        int: Factorial of n.
    """
    if n == 1:
        return 1

    return n * fatorial(n - 1)


def main():
    """
    Entry point of the program.
    """
    print(fatorial(6))


if __name__ == "__main__":
    main()