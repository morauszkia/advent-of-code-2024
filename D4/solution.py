class Puzzle:
    """
    A class to represent a grid-based word search puzzle. It provides methods
    to count occurrences of the word 'XMAS' in different directions and detect
    a special cross pattern involving 'MAS'.
    """

    def __init__(self, input_file):
        """
        Initializes the puzzle by reading a grid from the input file.

        Args:
            input_file (str): The name of the file containing the grid.

        Attributes:
            board (list of list of str): A 2D list representing the puzzle board.
            num_rows (int): The number of rows in the board.
            num_cols (int): The number of columns in the board.
            occurences_xmas (int): Counter for occurrences of the word "XMAS".
            occurences_cross (int): Counter for occurrences of the cross pattern.
            word (str): The target word to search ("XMAS").
        """
        with open(input_file, "r") as file:
            self.board = [list(line.strip()) for line in file]

        self.num_rows = len(self.board)
        self.num_cols = len(self.board[0])
        self.occurences_xmas = 0
        self.occurences_cross = 0
        self.word = "XMAS"

    def move(self, curr_row, curr_col, direction):
        """
        Moves a position in the specified direction.

        Args:
            curr_row (int): The current row position.
            curr_col (int): The current column position.
            direction (str): The direction to move in (e.g., "n", "se", "w").

        Returns:
            tuple: A tuple (new_row, new_col) representing the new position.
        """
        if "e" in direction:
            curr_col += 1
        if "w" in direction:
            curr_col -= 1
        if "n" in direction:
            curr_row -= 1
        if "s" in direction:
            curr_row += 1
        return (curr_row, curr_col)

    def is_invalid_coordinate(self, row, col):
        """
        Checks if a given coordinate is out of bounds.

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if the coordinate is invalid, False otherwise.
        """
        row_invalid = row < 0 or row >= self.num_rows
        col_invalid = col < 0 or col >= self.num_cols
        return row_invalid or col_invalid

    def found(self, direction, start_row, start_column):
        """
        Checks if the word 'XMAS' can be found starting from a given position
        in a specific direction.

        Args:
            direction (str): The direction to search (e.g., "n", "sw").
            start_row (int): The starting row index.
            start_column (int): The starting column index.

        Returns:
            bool: True if the word 'XMAS' is found in the given direction,
            False otherwise.
        """
        index = 1
        row = start_row
        col = start_column
        while True:
            row, col = self.move(row, col, direction)

            if self.is_invalid_coordinate(row, col):
                return False

            next_char = self.board[row][col]
            if next_char == self.word[index]:
                index += 1
                if index >= len(self.word):
                    return True
            else:
                return False

    def count_xmas(self):
        """
        Counts occurrences of the word 'XMAS' in all possible directions and
        updates the `occurences_xmas` attribute.

        Prints:
            The total count of occurrences of 'XMAS'.
        """
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col] == "X":
                    for direction in [
                        "n",
                        "s",
                        "e",
                        "w",
                        "ne",
                        "nw",
                        "se",
                        "sw",
                    ]:
                        self.occurences_xmas += self.found(direction, row, col)

        print(f"Solution 1: XMAS count: {self.occurences_xmas}")

    def get_diagonals(self, row, col):
        """
        Extracts two diagonal strings centered around a given 'A' character.

        Args:
            row (int): The row index of the 'A' character.
            col (int): The column index of the 'A' character.

        Returns:
            tuple: A tuple containing two diagonal strings.
        """
        diagonal1 = "".join(
            [self.board[row - 1][col - 1], "A", self.board[row + 1][col + 1]]
        )
        diagonal2 = "".join(
            [self.board[row - 1][col + 1], "A", self.board[row + 1][col - 1]]
        )

        return (diagonal1, diagonal2)

    def is_mas(self, word):
        """
        Checks if a given word is 'MAS' or its reverse.

        Args:
            word (str): The word to check.

        Returns:
            bool: True if the word is 'MAS' or 'SAM', False otherwise.
        """
        return word == "MAS" or word[::-1] == "MAS"

    def count_x_mas(self):
        """
        Counts occurrences of a cross pattern where 'A' is at the center and
        'MAS' appears diagonally in both directions.

        Prints:
            The total count of occurrences of the cross pattern.
        """
        for row in range(1, self.num_rows - 1):
            for col in range(1, self.num_cols - 1):
                if self.board[row][col] == "A":
                    d1, d2 = self.get_diagonals(row, col)
                    self.occurences_cross += self.is_mas(d1) and self.is_mas(
                        d2
                    )

        print(f"Solution 2: Number of X-MAS patterns: {self.occurences_cross}")


xmas_puzzle = Puzzle("input.txt")
xmas_puzzle.count_xmas()
xmas_puzzle.count_x_mas()
