class Rule:
    """
    Represents a rule that enforces an order between two elements in a list.
    """

    def __init__(self, rule_string):
        """
        Initializes a Rule object from a given rule string.

        Args:
            rule_string (str):  A string containing two numbers separated by
                                '|', indicating that the first number should
                                appear before the second in a list.

        Attributes:
            first (int): The first number in the rule.
            second (int): The second number in the rule.
        """
        first, second = rule_string.split("|")
        self.first = int(first)
        self.second = int(second)

    def applies(self, pages: list):
        """
        Checks if the rule applies to a given list.

        Args:
            pages (list of int): The list of numbers to check.

        Returns:
            bool: True if both numbers in the rule are present in the list,
            False otherwise.
        """
        return self.first in pages and self.second in pages

    def satisfied(self, pages: list):
        """
        Checks if the rule is satisfied in a given list.

        Args:
            pages (list of int): The list of numbers to check.

        Returns:
            bool: True if the first number appears before the second in the
            list, False otherwise.
        """
        return pages.index(self.first) < pages.index(self.second)


def parse_input(input_file):
    """
    Parses the input file and extracts sorting rules and lists.

    Args:
        input_file (str): The name of the input file.

    Returns:
        tuple:  A tuple (rules, lists) where:
                - rules (list of Rule): A list of Rule objects.
                - lists (list of list of int): A list of lists containing
                page numbers.
    """
    rules = []
    lists = []
    with open(input_file, "r") as file:
        for line in file:
            line_string = line.strip()
            if "|" in line_string:
                rules.append(Rule(line_string))
            elif "," in line_string:
                lists.append([int(num) for num in line_string.split(",")])

    return (rules, lists)


def get_middle(pages: list):
    """Returns the middle element of a given list."""
    return pages[len(pages) // 2]


def filter_relevant_rules(rules, lst):
    """
    Filters the rules that apply to a given list.

    Args:
        rules (list of Rule): A list of Rule objects.
        lst (list of int): The list of numbers.

    Returns:
        list: A list of Rule objects that apply to the given list.
    """
    return [r for r in rules if r.applies(lst)]


def correct_order(lst):
    """
    Reorders a list to satisfy all relevant rules.

    Args:
        lst (list of int): The list of numbers to reorder.

    Returns:
        list: The reordered list satisfying all applicable rules.
    """
    relevant_rules = filter_relevant_rules(rules, lst)
    while not all([r.satisfied(lst) for r in relevant_rules]):
        for r in relevant_rules:
            if not r.satisfied(lst):
                idx_1 = lst.index(r.first)
                idx_2 = lst.index(r.second)
                lst[idx_1], lst[idx_2] = lst[idx_2], lst[idx_1]
    return lst


rules, lists = parse_input("input.txt")

correct_lists = []
incorrect_lists = []

# Categorize lists based on rule satisfaction
for lst in lists:
    relevant_rules = filter_relevant_rules(rules, lst)
    if all([r.satisfied(lst) for r in relevant_rules]):
        correct_lists.append(lst)
    else:
        incorrect_lists.append(lst)

# Correct the order of incorrect lists
_ = [correct_order(lst) for lst in incorrect_lists]

print(f"Solution Part 1: {sum([get_middle(lst) for lst in correct_lists])}")
print(f"Aolution Part 2: {sum([get_middle(lst) for lst in incorrect_lists])}")
