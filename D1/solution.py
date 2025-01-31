def parse_input(filename):
    """
    Reads a file containing pairs of integers separated by triple spaces,
    extracts the numbers, and returns two sorted lists.

    Args:
        filename (str): The path to the input file.

    Returns:
        tuple: A tuple containing two sorted lists of integers.
    """
    first_list = []
    second_list = []
    with open(filename, "r") as f:
        for line in f:
            first, second = line.strip().split("   ")
            first_list.append(int(first))
            second_list.append(int(second))

    return (sorted(first_list), sorted(second_list))


def count_occurence(item, list):
    """
    Counts the occurrences of a given item in a list.

    Args:
        item (int): The item to count.
        list (list): The list in which to count occurrences.

    Returns:
        int: The number of times the item appears in the list.
    """
    count = 0
    for i in list:
        if item == i:
            count += 1
    return count


def calculate_similarity(list1, list2):
    """
    Calculates a similarity score between two lists by multiplying each element
    in list1 by the number of times it appears in list2 and summing the
    results.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        int: The similarity score.
    """
    similarity_score = 0
    for i in list1:
        similarity_score += i * count_occurence(i, list2)
    return similarity_score


first_list, second_list = parse_input("input.txt")

solution1 = sum([abs(f - s) for f, s in zip(first_list, second_list)])

solution2 = calculate_similarity(first_list, second_list)

print(f"Solution for Part 1 is : {solution1}")
print(f"Solution for Part 2 is : {solution2}")
