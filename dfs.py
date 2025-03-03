class DFSAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid  # The Wumpus World grid
        self.start = start  # Start position
        self.goal = goal  # Goal position
        self.visited = set()  # Set to keep track of visited nodes

    def dfs(self, position, path):
        if position == self.goal:
            return path  # Found the goal, return the path

        # Mark the current position as visited
        self.visited.add(position)

        # Possible directions to move: Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            new_position = (position[0] + direction[0], position[1] + direction[1])

            # Check if the new position is valid and not visited, and it's not a Wumpus or Pit
            if (0 <= new_position[0] < len(self.grid) and
                0 <= new_position[1] < len(self.grid[0]) and
                new_position not in self.visited and
                self.grid[new_position[0]][new_position[1]] != 'W' and
                self.grid[new_position[0]][new_position[1]] != 'P'):
                
                # Add the current position to the path and continue DFS
                new_path = path + [new_position]
                result = self.dfs(new_position, new_path)
                if result:
                    return result  # If the goal is found, return the path
        
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

# Create DFSAgent and run DFS
agent = DFSAgent(grid, start, goal)
path = agent.dfs(start, [start])

if path:
    print(f"Path found: {path}")
else:
    print("No path found")
