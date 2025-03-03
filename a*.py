import heapq

class Node:
    def __init__(self, position, g, h, parent=None):
        self.position = position  # (x, y) position in the grid
        self.g = g  # cost from the start node
        self.h = h  # heuristic cost to the goal node
        self.f = g + h  # total cost (f = g + h)
        self.parent = parent  # parent node
     
    def __lt__(self, other):
        return self.f < other.f  # for priority queue

def a_star(start, goal, grid):
    # Directions: Right, Left, Up, Down
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def heuristic(a, b):
        # Using Manhattan Distance as heuristic (can use other heuristics)
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = []
    closed_list = set()

    # Initialize the start node and add to open list
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get node with lowest f value
        current_node = heapq.heappop(open_list)
        
        if current_node.position == goal:
            # Reached goal, reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # reverse path to get start to goal

        closed_list.add(current_node.position)

        # Explore neighbors
        for direction in directions:
            neighbor = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])

            # Check if neighbor is within grid bounds and not a wall, Wumpus, or pit
            if (0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and
                    grid[neighbor[0]][neighbor[1]] != 'W' and grid[neighbor[0]][neighbor[1]] != 'P'):
                
                if neighbor in closed_list:
                    continue

                g_cost = current_node.g + 1  # assume uniform cost for each move
                h_cost = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

                # Add neighbor to open list
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

# Sample Wumpus World Grid (W = Wumpus, P = Pit, E = Empty, G = Goal)
# G is the goal, E is empty space, W is the Wumpus, P is the pit
grid = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E', 'P', 'E', 'W', 'E'],
    ['E', 'E', 'P', 'E', 'E'],
    ['E', 'W', 'E', 'P', 'E'],
    ['G', 'E', 'E', 'E', 'E']
]

# Start and Goal positions
start = (0, 0)
goal = (4, 0)

# Run A* to find the path
path = a_star(start, goal, grid)

if path:
    print(f"Path found: {path}")
else:
    print("No path found")
