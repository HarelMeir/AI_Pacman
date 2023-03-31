# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


############ Other functions ##################


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


class Node:
    """
    Class that defines node object.
    """

    def __init__(self, state):
        self.visited_list = []
        self.state = state

    def getVisitedList(self):
        return self.visited_list

    def getState(self):
        return self.state


def depthFirstSearch(problem):
    # DFS using stack
    stack = util.Stack()

    # lists for close list and path.
    close_list = []
    path = []

    # pushing the node into the list
    stack.push((problem.getStartState(), path))


    while stack:
        # pops an element with (x,y) coordinates at [0] and the path at [1]. simulates the Node object learned at class
        # location is the x,y coordinates, and path is the path so far.
        location, path = stack.pop()

        # adds the location to the close list, so we avoid loops.
        close_list.append(location)

        # if we reach our goal -> stops and returns the path.
        if problem.isGoalState(location):
            return path

        # get the "node" successors
        successors = problem.getSuccessors(location)

        # adds all the new sons(not gray) to the stack.
        for node in successors:
            if node[0] not in close_list:
                stack.push((node[0],path + [node[1]]))



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # BFS using queue
    queue = util.Queue()

    # lists for close list and path.
    close_list = []

    # pushing the node into queue
    queue.push(((problem.getStartState()), []))

    while not queue.isEmpty():
        # pops an element with (x,y) coordinates at [0] and the path at [1]. simulates the Node from class.
        (state, path) = queue.pop()

        # if we reach our goal -> stops and returns the path.
        if problem.isGoalState(state):
            return path

        # adds the location to the close list, so we avoid loops.
        close_list.append(state)

        # get the "node" successors
        successors = problem.getSuccessors(state)

        # adds all the new sons(not gray) to the stack.
        for next_node, action,step_cost in successors:
            if next_node not in close_list:
                close_list.append(next_node)
                queue.push((next_node, path + [action]))
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # create priority queue.
    pq = util.PriorityQueue()

    close_list = []
    path = []
                                     #
    pq.push((problem.getStartState(), path), 0)

    while not pq.isEmpty():
        # pops the lowest node from the pq.
        state, path = pq.pop()

        close_list.append(state)

        # if we reach our goal -> stops and returns the path.
        if problem.isGoalState(state):
            return path

        # get the next possible nodes from this state.
        successors = problem.getSuccessors(state)

        for next_node,action,step_cost in successors:
            # if its a new node -> pushing into pq.
            if next_node not in close_list and next_node not in pq.heap:
                pq.push((next_node, path + [action]), step_cost)

            # if the node already in the heap finds him, and getting its cost, and if the new cost smaller the last
            # cost, swap between them.
            elif next_node in pq.heap:
                for frontier_state in pq.heap:
                    if  frontier_state == next_node:
                        frontier_cost = problem.getCostOfActions(frontier_state)

                if step_cost < frontier_cost:
                    pq.update((next_node, path + [action]), step_cost)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    # create priority queue.
    pq = util.PriorityQueue()

    close_list = []

    pq.push(((problem.getStartState()), []), 0)

    while not pq.isEmpty():
        # pops the lowest node from the pq.
        state, path = pq.pop()
        close_list.append(state)

        # if we reach our goal -> stops and returns the path.
        if problem.isGoalState(state):
            return path

        # get the next possible nodes from this state.
        for next_node, action, step_cost in  problem.getSuccessors(state):
            if next_node not in close_list:
                close_list.append(next_node)
                total_cost = problem.getCostOfActions(path + [action]) + heuristic(next_node, problem)
                pq.push((next_node, path + [action]), total_cost)







# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
