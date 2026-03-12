import time

TEST_VALUES = [10, 100, 500, 1000]

def fatorial(n):
    """
    Calculates the factorial of a number using recursion.

    Args:
        n (int): Positive integer.

    Returns:
        int: Factorial of n.
    """
    if n <= 1:
        return 1

    return n * fatorial(n - 1)

def time_measurement(n):
    """
    Measures execution time of the factorial function.

    Args:
        n (int): Input value for factorial.

    Returns:
        float: Execution time in seconds.
    """
    start_time = time.time()
    fatorial(n)
    end_time = time.time()

    return end_time - start_time

def main():
    """
    Entry point of the program.
    Runs execution time tests for different values of n.
    """
    for n in TEST_VALUES:
        try:
            execution_time = time_measurement(n)
            print(f"n = {n} -> {execution_time:.8f} seconds")
        except RecursionError:
            print(f"n = {n} -> recursion limit reached")


if __name__ == "__main__":
    main()

