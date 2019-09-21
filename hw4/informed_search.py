# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
A* Algorithm and heuristics implementation

Your task for homework 4 is to implement:
1.  astar
2.  single_heuristic
3.  better_heuristic
4.  gen_heuristic
"""
import data_structures


def astar(problem, heuristic):
    """
    A* graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py
    heuristic (a function) the heuristic function to be used
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    # Enter your code here and remove the pass statement below
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, root.cumulative_cost)
    while True:
        if fringe.empty():
            return None  # Failure -  no solution was found
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node.actions()
        if node.state not in closed:  # we are implementing graph search
            closed.add(node.state)
            for child_state, action, action_cost in problem.expand(node.state):
                child_node = data_structures.Node(child_state, node, action)
                child_node.cumulative_cost = node.cumulative_cost + action_cost  # update cost of each child
                fringe.push(child_node, child_node.cumulative_cost)



def null_heuristic(state, problem):
    """
    Trivial heuristic to be used with A*.
    Running A* with this null heuristic, gives us uniform cost search
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: 0
    """
    return 0


def single_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return:
    """
    # Enter your code here and remove the pass statement below
    sammy, medal = state
    row_sammy, col_sammy = sammy
    row_medal, col_medal = medal
    manhattan = ((abs(row_sammy - row_medal), abs(col_sammy - col_medal)))


    return manhattan



def better_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    pass


def gen_heuristic(state, problem):
    """
    Fill in the docstring here
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return:
    """
    # Enter your code here and remove the pass statement below
    pass