from collections import deque

class BFSAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid  # The Wumpus World grid
        self.start = start  # Start position
        self.goal = goal  # Goal position

    def bfs(self):
        # Directions: Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Queue for BFS, stores (position, path_so_far)
        queue = deque([(self.start, [self.start])])
        visited = set()  # Set to keep track of visited nodes
        visited.add(self.start)

        while queue:
            current_position, path = queue.popleft()

            # If goal is found, return the path
            if current_position == self.goal:
                return path

            # Explore neighbors
            for direction in directions:
                new_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                # Check if new position is within grid bounds and not visited, and it's not a Wumpus or Pit
                if (0 <= new_position[0] < len(self.grid) and
                    0 <= new_position[1] < len(self.grid[0]) and
                    new_position not in visited and
                    self.grid[new_position[0]][new_position[1]] != 'W' and
                    self.grid[new_position[0]][new_position[1]] != 'P'):
                    
                    # Mark the new position as visited
                    visited.add(new_position)

                    # Add the new position to the queue with updated path
                    queue.append((new_position, path + [new_position]))

        return None  # No path found

# Sample Wumpus World Grid (W = Wumpus, P = Pit, E = Empty, G = Goal)
# G is the goal, E is empty space, W is the Wumpus, P is the pit
grid = [
    ['E', 'E', 'E', 'E', 'E'],
    ['E
