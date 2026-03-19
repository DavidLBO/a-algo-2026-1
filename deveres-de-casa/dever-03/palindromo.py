def palindromo(arr, inicio=0, fim=None):
    """Recursively checks if an array is a palindrome.

    An array is considered a palindrome when its elements are the same
    when read from left to right and from right to left.

    Args:
        arr (list): List of elements to be checked.
        inicio (int, optional): Starting index for comparison.
            Default is 0.
        fim (int, optional): Ending index for comparison.
            Default is the last index of the list.

    Returns:
        bool: True if the array is a palindrome, False otherwise.
    """
    if fim is None:
        fim = len(arr) - 1

    if inicio >= fim:
        return True

    if arr[inicio] != arr[fim]:
        return False

    return palindromo(arr, inicio + 1, fim - 1)


def main():
    """Runs example usages of the palindromo function."""
    exemplos = [
        [1, 2, 3, 2, 1],
        [1, 2, 3, 4, 5],
        ['a', 'b', 'b', 'a'],
        ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a'],
    ]

    for arr in exemplos:
        print(f"{arr} -> {palindromo(arr)}")


if __name__ == "__main__":
    main()