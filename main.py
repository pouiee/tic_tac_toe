import numpy as np
import random
import time

positions = [[0, 0], [0, 1], [0, 2],
             [1, 0], [1, 1], [1, 2],
             [2, 0], [2, 1], [2, 2]]


def two_player_turn(board):
    """
    main loop for manual tic-tac-toe, takes in user input for row and column to place in board array,
    uses function score to update board and determine winner, nonzero values will exit the game loop

    :param: board: np array of shape (3, 3) updated in score function
    :return: 0: game continues, 1: player 1 win, 2: player 2 win, 3: cat's game
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
            # Evaluate conditions where an invalid response may be received
            print("Please input a valid response(1,2,3)")
            p1_col, p1_row = '', ''
        elif board[int(p1_row) - 1][int(p1_col) - 1] != '':
            # determines if spot that player wishes to fill is occupied
            print("That spot is occupied, please try again.")
            p1_col, p1_row = '', ''

    # converts col and row into useful numbers for indexing
    # places player piece on board and displays, returns T/F for winner evaluation
    winner = score(board, 'X', int(p1_row) - 1, int(p1_col) - 1)

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
            # evaluate conditions where an invalid response may be received
            print("Please input a valid response(1,2,3)")
            p2_col, p2_row = '', ''
        elif board[int(p2_row) - 1][int(p2_col) - 1] != '':
            # determines if spot that player wishes to fill is occupied
            print("That spot is occupied, please try again.")
            p2_col, p2_row = '', ''

    # converts col and row into useful numbers for indexing
    # places player piece on board and displays,
    winner = score(board, 'O', int(p2_row) - 1, int(p2_col) - 1)

    if winner:  # evaluates if a winner has been chosen
        return 2

    if '' not in board:
        # ends game in a cat's game if no more space and no winner
        return 3

    # returns 0 code to continue loop
    return 0


def manual_game_loop():
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
            # user does not want to play, breaks loop
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
                two_player_turn(board)

            # evaluates various resulting conditions from the turn function
            if game_on == 1:
                # 1 means p1 is the winner
                print("Player 1 Wins! Play Again?")
            elif game_on == 2:
                # 2 means p2 is the winner
                print("Player 2 Wins! Play Again?")
            else:
                # 3 returned for a cat game
                print("Looks like a Cat's Game! Play Again?")
    # ambiguous goodbye message filled with character
    print("Well thanks for playing!")
    return 0


def score(board, p_num, p_row, p_col):
    """
    places p_num symbol (see player) in player-defined location in turn function and prints board
    then utilizes array comparison to determine if player has won as a result

    :param: board: np array of shape (3, 3)
    :param: p_num: 'X' or 'O'
    :param: p_row: number within limits (1, 2, or 3) denoting row in array
    :param: p_col: number within limits (1, 2, or 3) denoting column in array
    :return: boolean value True if a player has won, False otherwise
    """

    # places player's variable into selected position
    board[p_row][p_col] = p_num

    win_list = ['', '', '']  # list to compare against win condition
    win_con = [str(p_num), str(p_num), str(p_num)]  # establishes base win condition

    # places all p_num variables in list and evaluates win con in the | direction
    for n in range(3):
        win_list[n] = board[p_row][n]
    if win_list == win_con:
        return True

    # evaluates win con in the - direction
    for n in range(3):
        win_list[n] = board[n][p_col]
    if win_list == win_con:
        return True

    # evaluates win con in the / direction
    for n in range(3):
        win_list[n] = board[n][n]
    if win_list == win_con:
        return True

    # utilizes a helper integer 2 to traverse in the \ direction
    # evaluates win con in the \ direction
    for n in range(3):
        win_list[n] = board[n][2 - n]
    if win_list == win_con:
        return True

    # returns False after evaluating all possible win conditions
    return False


def seq_ai(p_num, board):
    """
    sequential AI will take turn, placing piece in the next available spot
    :param: board: np array of shape (3, 3) updated in score function
    :param: p_num: the player's number
    :return: 0: game continues, 1: player 1 win, 2: player 2 win, 3: cat's game
    """
    # iterates over positions list and sequentially tries different positions, starting over each time
    for pos in positions:
        # if the board is empty at that position
        if board[pos[0]][pos[1]] == '':
            # if the score function determines a winner has been found, return p_num
            if score(board, p_num, pos[0], pos[1]) is True:
                return p_num
            else:
                return 0

    # goes through each position and returns a 0 if an empty space remains
    for x in board:
        for y in x:
            if y == '':
                return 0

    # returns 3 if no winner is determined and no empty spaces remain
    return 3


def random_ai(p_num, board):
    """
    random selection of positions in board to take a turn
    :param: board: np array of shape (3, 3) updated in score function
    :param: p_num: the player's number
    :return: 0: game continues, 1: player 1 win, 2: player 2 win, 3: cat's game
    """
    rand_positions = positions
    random.shuffle(rand_positions)
    # utilizes rand_positions list to tries positions at random
    for pos in rand_positions:
        # if the board is empty at that position
        if board[pos[0]][pos[1]] == '':
            # if the score function determines a winner has been found, return p_num
            if score(board, p_num, pos[0], pos[1]) is True:
                return p_num
            else:
                return 0

    # goes through each position and returns a 0 if an empty space remains
    for x in board:
        for y in x:
            if y == '':
                return 0

    # returns 3 if no winner is determined and no empty spaces remain
    return 3


def auto_turn():
    """
    performs automatic turns using AI, tweak lines 243 and/or 245 to change which AI are in match
    NOTE: a sequential AI against a sequential AI will always result in a cat's game
    :return: 0 for normal execution
    """

    game_on = 0  # initialize game loop variable
    board = np.zeros((3, 3), dtype=str)  # initialize game board using '' strings

    while game_on == 0:
        game_on = seq_ai(1, board)
        if game_on == 0:
            game_on = random_ai(2, board)

    # evaluates various resulting conditions from the turn function
    if game_on == 1:
        # 1 means p1 is the winner
        game_on = 1, 0, 0
    elif game_on == 2:
        # 2 means p2 is the winner
        game_on = 0, 1, 0
    elif game_on == 3:
        # 3 returned for a cat game
        game_on = 0, 0, 1
    # returns a tuple x, x, x for incrementation of the win/draw variables
    return game_on


if __name__ == '__main__':
    # initialize variables needed, time log, various win counters, number of rounds
    time_log = []
    p_one_wins, p_two_wins, draws = 0, 0, 0
    rounds = 100000

    # start timing sequence
    begin = time.time()

    for i in range(rounds):
        # time an individual turn
        start = time.time()
        # return winning value and increment affiliated variable
        one_win, two_win, cat = auto_turn()
        # end turn timer and add turn to log
        stop = time.time()
        time_log.append(stop - start)
        # win counter increment
        p_one_wins += one_win
        p_two_wins += two_win
        draws += cat
    # ends timing sequence
    end = time.time()

    # debug information
    print(f"Total time elapsed: {round(end - begin, 2)} seconds.\n" +
          f"Average time per round: {round(sum(time_log) / rounds / .001, 4)} milliseconds")
    # statistics
    print(round(p_one_wins / rounds * 100, 2),
          round(p_two_wins / rounds * 100, 2),
          round(draws / rounds * 100, 2))
    print(f"{rounds} rounds")
