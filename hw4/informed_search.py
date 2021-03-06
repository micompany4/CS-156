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


def manhattan_with_cost(pos1, pos2, problem):
    """
    Manhattan distance with cost associated, used for better and general heuristic
    :param pos1: current position in terms of (x, y)
    :param pos2: objective position in terms of (x, y)
    :param problem: the problem object
    :return: the manhattan distance between two positions with cost associated
    """

    (r1, c1) = pos1
    (r2, c2) = pos2
    dy = r2 - r1
    dx = c2 - c1
    val = 0

    if dy < 0:
        val += abs(dy) * problem.cost['N']  # going north
    else:
        val += abs(dy) * problem.cost['S']  # going south
    if dx < 0:
        val += abs(dx) * problem.cost['W']  # going west
    else:
        val += abs(dx) * problem.cost['E']  # going east
    return val


def single_heuristic(state, problem):
    """
    The heuristic is an estimation to how far sammy is to a single medal
    based on sammy's manhattan distance (north, south, east, west, no diagonals) to that medal
<<<<<<< HEAD
    It is admissible because the manhattan distance does not consider the cost for taking
    a certain path, the cost is always 1 per move
    Therefore the heuristic cost will always be less than the actual cost
=======
    It is admissible because...
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
<<<<<<< HEAD
=======

>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
    :return: the manhattan distance from sammy to the goal as a heuristic
    """
    # Enter your code here and remove the pass statement below
    sammy, medal = state
<<<<<<< HEAD
    heuristic = 0
    if len(medal) == 0:
        return heuristic
    else:
        heuristic = manhattan(sammy, medal[0])

    return heuristic
=======
    if len(medal) == 0:     # means we have reached the goal state, set the heuristic value to 0
        return 0
    else:
        return manhattan(sammy, medal[0])
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d


def better_heuristic(state, problem):
    """
    A better heuristic to be used when we know for sure that there is only one medal in the quest.
    In this case, we account for the cost of each move unlike single_heuristic
    It is admissible because it will never exceed the actual cost, just equal to it at most
    It's better than single_heuristic because it will yield a value closer to the actual cost than single_heuristic
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: a heuristic that takes the cost for each move into consideration
    """
<<<<<<< HEAD
=======
    # Enter your code here and remove the pass statement below
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
    sammy, medal = state
    if len(medal) == 0:
        return 0
    return manhattan_with_cost(sammy, medal[0], problem)


def gen_heuristic(state, problem):
    """
    A more general heuristic to be used when the maze contains an arbitrary number of medals
    and these medals can be anywhere in the maze.
    Admissible because the manhattan distance with cost between sammy and a medal is always <= the actual cost
    since it represents a relaxed problem without the walls when we return the max, we are returning the longest
    path to get to a medal, and hoping to get as many medals on the way
    Consistent because since we are using the manhattan distance with cost, we know that the estimated cost
    of each node will be less than or equal to the actual cost. By this logic, we can see that the actual cost from
    node N to node N' added with the estimated cost of N' will always be greater than or equal the estimated cost of N
    :param
    state: A state is represented by a tuple containing:
                the current position (row, column) of Sammy the Spartan
                a tuple containing the positions of the remaining medals
    problem: (a Problem object) representing the quest
    :return: The maximum manhattan distance with cost of all medals
    """
<<<<<<< HEAD
    (sammy, medal) = state
    if not medal:
        return 0
    return max(manhattan_with_cost(sammy, m, problem) for m in medal)


def manhattan(pos1, pos2):
    """
    Manhattan distance, used for single heuristic
    Given two positions find the lateral distance and vertical distance between them
    :param pos1: current position in terms of (x, y)
    :param pos2: objective position in terms of (x, y)
    :return: the manhattan distance between two positions
    """
    row1, col1 = pos1
    row2, col2 = pos2

    return abs(row1 - row2) + abs(col1 - col2)


def manhattan_with_cost(pos1, pos2, problem):
    """
    Manhattan distance with cost associated, used for better and general heuristic
    :param pos1: current position in terms of (x, y)
    :param pos2: objective position in terms of (x, y)
    :param problem: the problem object
    :return: the manhattan distance between two positions with cost associated
    """

    (r1, c1) = pos1
    (r2, c2) = pos2
    dy = r2 - r1
    dx = c2 - c1
    val = 0

    if dy < 0:
        val += abs(dy) * problem.cost['N']  # going north
    else:
        val += abs(dy) * problem.cost['S']  # going south
    if dx < 0:
        val += abs(dx) * problem.cost['W']  # going west
    else:
        val += abs(dx) * problem.cost['E']  # going east
    return val
=======
    # Enter your code here and remove the pass statement below
    sammy, medals = state
    total = 0
    r1, c1 = sammy
    dx = 0
    dy = 0
    if len(medals) == 0:
        return 0

    for m in medals:
        r2, c2 = m
        dx = r2 - r1
        dy = c2 - c1

        if dx < 0:
            dx = abs(dx) * 4  # moving in north direction
        else:
            dx = abs(dx) * 3  # moving in south direction
        if dy < 0:
            dy = abs(dy) * 1  # moving in west direction
        else:
            dy = abs(dy) * 5  # moving in east direction

        total += dx + dy

    return total/40
>>>>>>> 583f43dbc295ad922cee2ba64de0c3e4049a3a4d
