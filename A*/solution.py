#!/usr/bin/python3

# CS-E4800 AI, Programming assignment round 2: A*.
# Fill in the code sections marked with "TODO"

# Do not add any imports: they will be ignored in the grading environment.
from queue import PriorityQueue
import math
from parsing import read_instance

def astar(coords, adj, start, goal):

    # Nodes are numbered from 1 to n; 
    # 0 is a dummy node with no edges
    n = len(coords) - 1
    
    # Initialize tables
    
    # prev[x]: the previous node on the
    # shortest path found so far from start to x
    prev = [i for i in range(n+1)]
    
    mindist = [math.inf for i in range(n+1)]
    
    # Heuristic function
    
    def heur(pos1, pos2):
        x1,y1 = pos1
        x2,y2 = pos2
        # TODO: replace with a better heuristic function
        return min(abs(x1-x2),abs(y1-y2))

    # Memoization: compute heuristics on demand and only once
    _heur = [-1] * (n+1)
    def get_heur(i):
        if _heur[i] == -1:
            pos = coords[i]
            _heur[i] = heur(coords[i],coords[goal])
        return _heur[i]
        
    # Initialize BFS
        
    queue=PriorityQueue()
    found = False
    mindist[start]=0
    # TODO: insert the starting position into the queue

    # Main loop for processing the queue
    
    while not queue.empty():
        (_,node) = queue.get()
        # TODO: exit early if you can prove you've 
        # found the optimal path from start to goal
        for (next,l) in adj[node]:
            # next: a neighbor of 'node'
            # l: the distance from 'node' to 'next'
            # TODO: decide if any of the node's neighbors
            # should be explored (added to the queue).
            pass # To be removed

    # If the goal was found, unwind the path

    if found:
        # TODO: Extract the solution and return it as a list of nodes [start,...,goal]
        pass # To be removed
    else:
        return None
        
