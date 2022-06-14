import numpy as np


def score(board, player, p_row, p_col):
    """
    places player symbol (see player) in player-defined location in turn function and prints board
    then utilizes array comparison to determine if player has won as a result

    :param board: np array of shape (3, 3)
    :param player: 'X' or 'O'
    :param p_row: number within limits (1, 2, or 3) denoting row in array
    :param p_col: number within limits (1, 2, or 3) denoting column in array
    :return: boolean value True if a player has won, False otherwise
    """

    # places player's variable into selected position
    board[p_row][p_col] = player
    # displays board after new move, flipping board for human viewing
    print(np.flipud(board))

    win_list = ['', '', '']  # list to compare against win condition
    win_con = [player, player, player]  # establishes base win condition

    # places all player variables (or '') in list and evaluates win con in the | direction
    for num in range(3):
        win_list[num] = board[p_row][num]
    if win_list == win_con:
        return True
    # evaluates win con in the - direction
    for num in range(3):
        win_list[num] = board[num][p_col]
    if win_list == win_con:
        return True
    # evaluates win con in the / direction
    for num in range(3):
        win_list[num] = board[num][num]
    if win_list == win_con:
        return True
    # utilizes a helper variable to traverse in the \ direction
    diagonal_helper = 2
    # evaluates win con in the \ direction
    for num in range(3):
        win_list[num] = board[num][diagonal_helper - num]
    if win_list == win_con:
        return True

    # returns False after evaluating all possible win conditions
    return False


def turn(board):
    """
    main loop for tic tac toe, takes in user input for row and column to place in board array,
    uses function score to update board and determine winner, nonzero values will exit the game loop

    :param board: np array of shape (3, 3) updated in score function
    :return: 0: no winner or cat's game, 1: player 1 win, 2: player 2 win, 3: cat's game
    """
    print("Player 1, your move.")

    # columns and rows numbered 1-3 for user ease
    limits = ['1', '2', '3']
    # initialize empty string column and row string for player 1
    p1_col, p1_row = '', ''

    while p1_col == '' or p1_row == '':
        # user selects column and row to place marker 'X'
        p1_row = input("Row? ")
        p1_col = input("Column? ")

        if p1_col not in limits or p1_row not in limits:
            # evaluates conditions where an invalid response may be received
            print("Please input a valid response(1,2,3)")
            p1_col, p1_row = '', ''
        elif board[int(p1_row) - 1][int(p1_col) - 1] != '':
            # determines if spot that player wishes to fill is occupied
            print("That spot is occupied, please try again.")
            p1_col, p1_row = '', ''

    # converts col and row into useful numbers for indexing
    # places player piece on board and displays, returns T/F for winner evaluation
    winner = score(board, 'X', int(p1_row)-1, int(p1_col)-1)

    if winner:  # evaluates if a winner has been chosen
        return 1

    if '' not in board:
        # ends game in a cat's game if no more space and no winner
        return 3

    print("Player 2, your move.")
    # initialize empty string column and row string for player 2
    p2_col, p2_row = '', ''

    while p1_col == '' or p2_row == '':
        # user selects column and row to place marker 'X'
        p2_row = input("Row? ")
        p2_col = input("Column? ")

        if p2_col not in limits or p2_row not in limits:
            # evaluates conditions where an invalid response may be received
            print("Please input a valid response(1,2,3)")
            p2_col, p2_row = '', ''
        elif board[int(p2_row) - 1][int(p2_col) - 1] != '':
            # determines if spot that player wishes to fill is occupied
            print("That spot is occupied, please try again.")
            p2_col, p2_row = '', ''

    # converts col and row into useful numbers for indexing
    # places player piece on board and displays,
    winner = score(board, 'O', int(p2_row)-1, int(p2_col)-1)

    if winner:  # evaluates if a winner has been chosen
        return 2

    if '' not in board:
        # ends game in a cat's game if no more space and no winner
        return 3

    # returns 0 code to continue loop
    return 0


def game_loop():
    """
    starts game loop, continues as long as the user wants to play,
    detects valid inputs then initializes game board and starts game
    whole game can be bypassed with a simple n or N

    :return: 0 for executing normally
    """
    print("Would you like to play a game?")
    print("It's a two player game so bring a friend or just pretend you have one.")
    play_time = ''
    while play_time.upper() != 'N':
        play_time = input("Well? (Y / N): ")
        if play_time.upper() == 'N':
            # user does not want to play.. breaks loop
            break
        elif play_time.upper() != 'Y':
            # user enters incorrect response, returns to beginning of loop
            print("Please select a valid response (Y / N)")
            continue
        else:
            # user wants to play, initializes game board
            board = np.zeros((3, 3), dtype=str)
            print(board)  # displays empty board for user
            # game_on variable used to evaluate conditions returned from turn
            game_on = 0
            print("Good Luck! Remember, Columns and Rows are 1, 2, 3.")
            # user assistance for game rules
            while game_on == 0:
                # game loop
                game_on = turn(board)

            # evaluates various resulting conditions from the turn function
            if game_on == 1:
                # 1 means p1 is the winner
                print("Player 1 Wins! Play Again?")
            elif game_on == 2:
                # 2 means p2 is the winner
                print("Player 2 Wins! Play Again?")
            else:
                # 3 returned for a cat game (but return value is irrelevant)
                print("Looks like a Cat's Game! Play Again?")
    # ambiguous goodbye message filled with character
    print("Well thanks for playing!")
    return 0

if __name__ == '__main__':
    game_loop()
