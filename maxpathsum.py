import random


def find_max_path(board):
    """

    Arguments:
        board (list[list[int]]): The n*m grid with cell values.

    Returns:
        tuple (int, list[tuple]): 
            - The maximum value.
            - The list of (row, col) coordinates representing the path.
    """
    if not board or not board[0]:
        return 0, []

    n = len(board)
    m = len(board[0])

    #Create and fill the DP table
    dp = [[0 for _ in range(m)] for _ in range(n)]

    #Base Case
    dp[0][0] = board[0][0]

    #Fill first row which comes from the left
    for j in range(1, m):
        dp[0][j] = board[0][j] + dp[0][j - 1]

    #Fill first column which comes from the top
    for i in range(1, n):
        dp[i][0] = board[i][0] + dp[i - 1][0]

    #Fill the rest
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = board[i][j] + max(
                dp[i - 1][j],  # From top
                dp[i][j - 1],  # From left
                dp[i - 1][j - 1]  # From diagonal
            )

    #Reconstruct the path by backtracking
    path = []
    i, j = n - 1, m - 1

    while i >= 0 and j >= 0:
        path.append((i, j))

        if i == 0 and j == 0:
            break  # Reached the start

        #Check which cell
        #Handle edge cases (first row/col) first
        if i == 0:
            j -= 1  #Comes from left
        elif j == 0:
            i -= 1  #Comes from top
        else:
            #Check general case, prioritizing diagonal, then top, then left
            prev_val = dp[i][j] - board[i][j]

            if prev_val == dp[i - 1][j - 1]:
                i, j = i - 1, j - 1
            elif prev_val == dp[i - 1][j]:
                i -= 1
            else:
                j -= 1

    #The path was built backward, so reverse it
    max_value = dp[n - 1][m - 1]
    return max_value, path[::-1]


#Testing function
def generate_test_board(n, m, min_val=-10, max_val=50):
    """Generates a random n*m board."""
    return [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]


def print_board(board):
    """Utility to print the board neatly."""
    for row in board:
        print(" ".join(f"{val:3}" for val in row))