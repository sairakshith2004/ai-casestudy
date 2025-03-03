import heapq

class UCSAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid  # The Wumpus World grid
        self.start = start  # Start position
        self.goal = goal  # Goal position

    def ucs(self):
        # Directions: Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Priority Queue (Min-Heap) to explore nodes with lowest cost first
        open_list = []
        heapq.heappush(open_list, (0, self.start, [self.start]))  # (cost, position, path)
        visited = set()  # Set to keep track of visited nodes

        while open_list:
            current_cost, current_position, path = heapq.heappop(open_list)

            # If goal is found, return the path
            if current_position == self.goal:
                return path

            if current_position in visited:
                continue

            # Mark the current position as visited
            visited.add(current_position)

            # Explore neighbors
            for direction in directions:
                new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                # Check if the new position is within grid bounds and not a Wumpus or Pit
                if (0 <= new_position[0] < len(self.grid) and
                    0 <= new_position[1] < len(self.grid[0]) and
                    new_position not in visited and
                    self.grid[new_position[0]][new_position[1]] != 'W' and
                    self.grid[new_position[0]][new_position[1]] != 'P'):
                    
                    # Add the new position to the priority queue with updated cost and path
                    heapq.heappush(open_list, (current_cost + 1, new_position, path + [new_position]))

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

# Create UCSAgent and run UCS
agent = UCSAgent(grid, start, goal)
path = agent.ucs()

if path:
    print(f"Path found: {path}")
else:
    print("No path found")
