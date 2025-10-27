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
            # --- THIS IS THE FIX ---
            # The order in max() must match the if/elif/else order below.
            dp[i][j] = board[i][j] + max(
                dp[i - 1][j - 1],  # From diagonal (Preference 1)
                dp[i - 1][j],      # From top (Preference 2)
                dp[i][j - 1]       # From left (Preference 3)
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
            # This logic now matches the max() preference order exactly.
            prev_val = dp[i][j] - board[i][j]

            if prev_val == dp[i - 1][j - 1]:
                i, j = i - 1, j - 1  # Preference 1
            elif prev_val == dp[i - 1][j]:
                i -= 1               # Preference 2
            else:
                j -= 1               # Preference 3

    #The path was built backward, so reverse it
    max_value = dp[n - 1][m - 1]
    return max_value, path[::-1]
#Testing functions
def generate_test_board(n, m, min_val=-10, max_val=50):
    """Generates a random n*m board."""
    return [[random.randint(min_val, max_val) for _ in range(m)] for _ in range(n)]


def print_board(board):
    """Utility to print the board neatly."""
    for row in board:
        print(" ".join(f"{val:3}" for val in row))

#Main
if __name__ == "__main__":
    #Test 1: Small 3x3 Random Board
    print("--- Test Case 1: 3x3 Random Board ---")
    board1 = generate_test_board(3, 3, min_val=-10, max_val=20)
    print("Board:")
    print_board(board1)
    max_val1, path1 = find_max_path(board1)
    print(f"\nMaximum Value: {max_val1}")
    print(f"Path: {path1}\n")

    #Test 2: 4x5 Random Board
    print("--- Test Case 2: 5x7 Random Board ---")
    board2 = generate_test_board(5, 7, min_val=-20, max_val=20)
    print("Board:")
    print_board(board2)
    max_val2, path2 = find_max_path(board2)
    print(f"\nMaximum Value: {max_val2}")
    print(f"Path: {path2}\n")

    #Test 3: 5x4 Random Board
    print("--- Test Case 3: 4x14 Random Board ---")
    board3 = generate_test_board(4, 14, min_val=0, max_val=30)
    print("Board:")
    print_board(board3)
    max_val3, path3 = find_max_path(board3)
    print(f"\nMaximum Value: {max_val3}")
    print(f"Path: {path3}\n")