def find_next_empty(puzzle):
    # finds next row, col on the puzzle that is not filled yet! --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None  # if no spaces in the puzzle are empty


def is_valid(puzzle, guess, row, col):
    # Figures out if guess at the row/col is valid guess
    # return True if valid, otherwise false

    # First let's check the row
    row_values = puzzle[row]
    if guess in row_values:
        return False
    # Now let's check the column
    # col_values = []
    # for i in range(9):
    #     col_values.append(puzzle[i][col])
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False

    # and then the square
    # this is tricky, but we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3  # 1//3 = 0, 5//3 = 1
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[c][r] == guess:
                return False

    # if we get here, the check passes
    return True


def solve_sudoku(puzzle):
    # solve sudoku using backtracking
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exits)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # Step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:
        return True

    # Step 2: if there is a place to put our number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # Step 3: Check if guess is valid
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is valid, then place that guess on that puzzle!
            puzzle[row][col] = guess
            # now recurse using this puzzle!
            # step 4: recursively call our function
            if solve_sudoku(puzzle):
                return True

        # Step 5: if not valid OR if our guess does not solve the puzzle, then we need to
        # backtrack and try a new number
        puzzle[row][col] = -1  # reset the guess
    # Step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False
