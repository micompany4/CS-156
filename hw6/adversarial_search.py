# ----------------------------------------------------------------------
# Name:     adversarial_search
# Purpose:  Homework 6 - Implement adversarial search algorithms
#
# Author:
#
# ----------------------------------------------------------------------
"""
Adversarial search algorithms implementation

Your task for homework 6 is to implement:
1.  minimax
2.  alphabeta
3.  abdl (alpha beta depth limited)
"""
import random
import math  # You can use math.inf to initialize to infinity
import math


def rand(game_state):
    """
    Generate a random move.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the random move
    """
    done = False
    while not done:
        row = random.randint(0, game_state.size - 1)
        col = random.randint(0, game_state.size - 1)
        if game_state.available(row,col):
            done = True
    return row, col


def minimax(game_state):
    """
    Find the best move for our AI agent using the minimax algorithm.
    (searching the entire tree from the current game state)
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    # return max(value(game_state.successor(m, 'AI'), 'user') for m in game_state.possible_moves())
    return max(game_state.possible_moves(), key=lambda node: value(game_state.successor(node, 'AI'), 'user'))


def value(game_state, agent):
    """
    Calculate the minimax value for any state under the given agent's
    control.
    :param game_state: GameState object - state may be terminal or
    non-terminal
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    if game_state.is_win('AI'):
        return 1
    elif game_state.is_tie():
        return 0
    elif game_state.is_win('user'):
        return -1
    elif agent is 'AI':
        return max_value(game_state)
    else:
        return min_value(game_state)


def max_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    # return max(game_state.possible_moves(), key=lambda m: value(game_state.successor(m, 'AI'), 'user'))
    return max(value(game_state.successor(m, 'AI'), 'user') for m in game_state.possible_moves())


def min_value(game_state):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user)
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    # return min(game_state.possible_moves(), key=lambda m: value(game_state.successor(m, 'user'), 'AI'))
    return min(value(game_state.successor(m, 'user'), 'AI') for m in game_state.possible_moves())


def alphabeta(game_state):
    """
    Find the best move for our AI agent using the minimax algorithm
    with alpha beta pruning.
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    return max(game_state.possible_moves(), key=lambda node: ab_value(game_state.successor(node, 'AI'), 'user',
                                                                      -math.inf, math.inf))


def ab_value(game_state, agent, alpha, beta):
    """
    Calculate the minimax value for any state under the given agent's
    control using alpha beta pruning
    :param game_state: GameState object - state may be terminal or
    non-terminal.
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    if game_state.is_win('AI'):
        return 1
    elif game_state.is_tie():
        return 0
    elif game_state.is_win('user'):
        return -1
    elif agent is 'AI':
        return abmax_value(game_state, alpha, beta)
    else:
        return abmin_value(game_state, alpha, beta)


def abmax_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Max's
    control (AI agent) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    v = -math.inf
    for s in game_state.possible_moves():
        v = max(v, ab_value(game_state.successor(s, 'AI'), 'user', alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v


def abmin_value(game_state, alpha, beta):
    """
    Calculate the minimax value for a non-terminal state under Min's
    control (user) using alpha beta pruning
    :param game_state: non-terminal GameState object
    :return: (integer) value of that state -1, 0 or 1
    """
    # Enter your code here and remove the pass statement below
    v = math.inf
    for s in game_state.possible_moves():
        v = min(v, ab_value(game_state.successor(s, 'user'), 'AI', alpha, beta))
        if v <= alpha:
            return v
        beta = max(beta, v)
    return v


def abdl(game_state, depth):
    """
    Find the best move for our AI agent by limiting the alpha beta
    search the given depth and using the evaluation function
    game_state.eval()
    :param game_state: GameState object
    :return:  a tuple representing the row column of the best move
    """
    # Enter your code here and remove the raise statement below
    raise NotImplementedError



def abdl_value(game_state, agent, alpha, beta, depth):
    """
    Calculate the utility for any state under the given agent's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: GameState object - state may be terminal or
    non-terminal
    :param agent: (string) 'user' or 'AI' - AI is max
    :return: (integer) utility of that state
    """
    # Enter your code here and remove the pass statement below
    pass


def abdlmax_value(game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Max's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    pass


def abdlmin_value( game_state, alpha, beta, depth):
    """
    Calculate the utility for a non-terminal state under Min's control
    using depth limited alpha beta pruning and the evaluation
    function game_state.eval()
    :param game_state: non-terminal GameState object
    :return: (integer) utility (evaluation function) of that state
    """
    # Enter your code here and remove the pass statement below
    pass

