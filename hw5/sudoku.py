# ----------------------------------------------------------------------
# Name:     sudoku
# Purpose:  Homework5
#
<<<<<<< HEAD
# Author(s):
=======
# Author(s): Michael Wong, Joseph Nguyen
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
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

<<<<<<< HEAD
=======

>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
def build_csp(puzzle):
    """
    Create a CSP object representing the puzzle.
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: CSP object
    """
    # Enter your code here and remove the pass statement below
<<<<<<< HEAD
    pass
=======
    csp_object = csp(puzzle, {'key': 2.23, 'seed': 9.43}, 0) # some random values
    return csp_object
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d


def q1(puzzle):
    """
    Solve the given puzzle with basic backtracking search
    :param puzzle (dictionary): The dictionary keys are tuples
    (row, column) representing the filled puzzle squares and the values
    are the corresponding numbers assigned to these squares.
    :return: a tuple consisting of a solution (dictionary) and the
    CSP object.
    """
    # Enter your code here and remove the pass statement below
<<<<<<< HEAD
    pass
=======
    csp_obj = build_csp(puzzle)
    result = (csp_obj.backtracking_search(), csp_obj)

    return result

>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d

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
    # Enter your code here and remove the pass statement below
<<<<<<< HEAD
    pass
=======
    csp_obj = build_csp(puzzle)
    csp_obj.ac3_algorithm()
    result = (csp_obj.backtracking_search(), csp_obj)

    return result
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d

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
    # Enter your code here and remove the pass statement below
<<<<<<< HEAD
    pass
=======
    csp_obj = build_csp(puzzle)
    csp_obj.ac3_algorithm()
    result = (csp_obj.backtracking_search("MRV"), csp_obj)

    return result
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
