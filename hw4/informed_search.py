# ----------------------------------------------------------------------
# Name:     informed_search
# Purpose:  Homework 4 - Implement astar and some heuristics
#
# Author(s): Michael Wong, Joseph Nguyen
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
    fringe = data_structures.PriorityQueue()  # for astar, the fringe is a priority queue
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root, root.cumulative_cost + heuristic(state, problem))  # priority cost + heuristic
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
                fringe.push(child_node, child_node.cumulative_cost + heuristic(child_state, problem))


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


def manhattan(pos1, pos2):
    """
    finds the manhattan distance between two objects based on their (x, y) positions
    :param pos1: current position in terms of (x, y)
    :param pos2: objective position in terms of (x, y)
    :return: the manhattan distance between two positions
    """
    # unpack the position tuples
    row1, col1 = pos1
    row2, col2 = pos2

    return abs(row1 - row2) + abs(col1 - col2)


def single_heuristic(state, problem):
    """
    The heuristic is an estimation to how far sammy is to a single medal
    based on sammy's manhattan distance (north, south, east, west, no diagonals) to that medal
    It is admissible because...
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest

    :return: the manhattan distance from sammy to the goal as a heuristic
    """
    # Enter your code here and remove the pass statement below
    sammy, medal = state
    if len(medal) == 0:     # means we have reached the goal state, set the heuristic value to 0
        return 0
    else:
        return manhattan(sammy, medal[0])


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
    sammy, medal = state
    if len(medal) == 0:
        return 0
    
    r1, c1 = sammy
    r2, c2 = medal[0]

    # manhattan distance for east/west and north/south
    d1 = r1 - r2
    d2 = c1 - c2

    if d1 > 0:
        d1 = abs(d1) * 4    # moving in north direction
    else:
        d1 = abs(d1) * 3    # moving in south direction

    if d2 > 0:
        d2 = abs(d2) * 1    # moving in west direction
    else:
        d2 = abs(d2) * 5    # moving in east direction

    return d1 + d2


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
