import re


def read_input(filename):
    """
    Reads the contents of a file and returns it as a string.
    """
    with open(filename, "r") as f:
        return f.read()


def extract_commands(str, mul_only=False):
    """
    Extracts specific commands from a given string using regex.

    Args:
        string (str): The input string containing commands.
        mul_only (bool, optional): If True, extracts only "mul(x,y)" commands.
                                   If False, extracts "mul(x,y)", "don't()",
                                   and "do()" commands.
                                   Defaults to False.

    Returns:
        list of str: A list of extracted commands matching the regex pattern.
    """
    regex = (
        r"mul\(\d+,\d+\)" if mul_only else r"mul\(\d+,\d+\)|don't\(\)|do\(\)"
    )
    matches = re.findall(regex, str)
    return matches


def evaluate_multiplication(command):
    """
    Evaluates a multiplication command of the form "mul(x,y)" and returns the
    product.
    """
    num1, num2 = re.findall(r"\d+", command)
    return int(num1) * int(num2)


corrupted_code = read_input("input.txt")
multiplications = extract_commands(corrupted_code, mul_only=True)
commands = extract_commands(corrupted_code)

sum_p1 = 0
for m in multiplications:
    sum_p1 += evaluate_multiplication(m)

print(f"Solution Part One: {sum_p1}")

sum_p2 = 0
enabled = True
for c in commands:
    if c == "don't()":
        enabled = False
    elif c == "do()":
        enabled = True
    elif "mul" in c and enabled:
        sum_p2 += evaluate_multiplication(c)

print(f"Solution Part Two: {sum_p2}")
