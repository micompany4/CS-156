# ----------------------------------------------------------------------
# Name:     uninformed_search
# Purpose:  Homework3 - Implement bfs and ucs graph search algorithms
#
# Author(s):
#
# ----------------------------------------------------------------------
"""
Uninformed Search Algorithm implementation

dfs has been implemented for you.
Your task for homework 3 is to implement bfs and ucs.
"""
import data_structures

def dfs(problem):
    """
    Depth first graph search algorithm - implemented for you
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py)
    :return: list of actions representing the solution to the quest
                or None if there is no solution
    """
    closed = set()  # keep track of our explored states
    fringe = data_structures.Stack() # for dfs, the fringe is a stack
    state = problem.start_state()
    root = data_structures.Node(state)
    fringe.push(root)
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
                fringe.push(child_node)



def bfs(problem):
    """
    Breadth first graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py)
    :return: list of actions representing the solution to the quest
            or None if there is no solution
    """
    # Enter your  code here and remove the pass statement below
    closed = set()  # tracks the states that we have explored
    fringe = data_structures.Queue()  # bfs utilizes a queue
    root = data_structures.Node(problem.start_state())  # makes a node that holds the initial state of the problem
    fringe.push(root)  # places the node into the fringe

    while True:
        if fringe.empty():  # if the fringe is empty, then no solution could be found
            return None
        node = fringe.pop()  # get the first node on from the fringe
        if problem.is_goal(node.state):  # if we reached our goal, return the path we took
            return node.actions()
        if node.state not in closed:  # if we haven't seen this state, add it to the closed set
            closed.add(node.state)

            # look to its children for more possible paths
            for child_state, action, action_cost in problem.expand(node.state):
                child_node = data_structures.Node(child_state, node, action)
                fringe.push(child_node)


def ucs(problem):
    """
    Uniform cost first graph search algorithm
    returns a solution for the given search problem
    :param
    problem (a Problem object) representing the quest
            see Problem class definition in spartanquest.py)
    :return: list of actions representing the solution to the quest
    """
    # Enter your code here and remove the pass statement below
    closed = set()  # keep track of our explored states
    fringe = data_structures.PriorityQueue()  # for ucs, the fringe is a priority queue
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

