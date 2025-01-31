def calculate_differences(numbers):
    """
    Computes the differences between consecutive elements in a list.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing the differences between consecutive
        numbers.
    """
    differences = []
    for i in range(1, len(numbers)):
        differences.append(numbers[i] - numbers[i - 1])
    return differences


def are_safe(numbers):
    """
    Determines if a sequence of numbers is "safe" based on the condition that
    all consecutive differences are either strictly positive and at most 3,
    or strictly negative and at least -3.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        bool: True if the sequence is safe, False otherwise.
    """
    diffs = calculate_differences(numbers)
    return all([d > 0 and d <= 3 for d in diffs]) or all(
        [d < 0 and d >= -3 for d in diffs]
    )


def is_dampenable(numbers):
    """
    Checks whether a sequence can be made "safe" by removing at most one
    element.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        bool: True if the sequence can be made safe by removing one element,
        False otherwise.
    """
    for i in range(len(numbers)):
        altered_list = numbers.copy()
        altered_list.pop(i)
        if are_safe(altered_list):
            return True
    return False


def process_input(path):
    """
    Reads an input file containing sequences of numbers, checks whether each
    sequence is safe or can be made safe by removing one element, and prints
    the results.

    Args:
        path (str): The path to the input file.

    Prints:
        - Number of safe sequences.
        - Number of dampened (fixable) sequences.
        - Total number of safe sequences (safe + dampened).
    """
    safe_lines = 0
    dampened_lines = 0
    with open(path, "r") as f:
        for line in f:
            numbers = [int(n) for n in line.strip().split(" ")]
            if are_safe(numbers):
                safe_lines += 1
            elif is_dampenable(numbers):
                dampened_lines += 1
    print(f"Number of safe lines: {safe_lines}")
    print(f"Dampened lines: {dampened_lines}")
    print(f"Total number of safe lines: {safe_lines + dampened_lines}")


process_input("input.txt")
