# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework5
#
# Author(s): Joseph Nguyen, Michael Wong
#
# ----------------------------------------------------------------------
"""
Sudoku puzzle solver implementation

q1:  Basic Backtracking Search
q2:  Backtracking Search with AC-3
q3:  Backtracking Search with MRV Ordering and AC-3
"""
import csp


# Enter your helper functions here

def build_csp(puzzle):
    """
    Create a CSP object representing the puzzle.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: CSP object
    """
    indexes = []
    for i in range(0, 9):
        for j in range(0, 9):
            indexes.append((i, j))

    index_domains = {}
    for i in indexes:
        if i in puzzle:
            index_domains[i] = {puzzle[i]}
        else:
            index_domains[i] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    index_neighbors = {}
    for i in indexes:
        (row, col) = i

        #  regions
        row_min = row // 3 * 3  # gives the starting index of region
        col_min = col // 3 * 3
        neighbors = region(row_min, col_min)

        #  rows and columns
        for j in range(0, 9):
            neighbors.add((row, j))
            neighbors.add((j, col))

        neighbors = neighbors - {i}  # remove itself from neighbors
        index_neighbors[i] = neighbors

    return csp.CSP(index_domains, index_neighbors, constraint)


def constraint(var1, val1, var2, val2):
    return not val1 == val2


def region(row_min, col_min):
    tuple_set = set()
    for i in range(row_min, row_min + 3):
        for j in range(col_min, col_min + 3):
            tuple_set.add((i, j))
    return tuple_set


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    the_csp = build_csp(puzzle)
    solution = the_csp.backtracking_search()
    return solution, the_csp


def q2(puzzle):
    """
    Solve the given puzzle with backtracking search and AC-3 as
    a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    the_csp = build_csp(puzzle)
    the_csp.ac3_algorithm()
    solution = the_csp.backtracking_search()
    return solution, the_csp


def q3(puzzle):
    """
    Solve the given puzzle with backtracking search and MRV ordering and
    AC-3 as a preprocessing step.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    the_csp = build_csp(puzzle)
    the_csp.ac3_algorithm()
    solution = the_csp.backtracking_search("MRV")
    return solution, the_csp
