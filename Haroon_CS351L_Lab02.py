# Function to move obstacles randomly after each step
def move_obstacles(grid, obstacles):
    size = len(grid)
    new_obstacles = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible movement directions
    
    for (x, y) in obstacles:
        grid[x][y] = ' '  # Remove the old obstacle
        
        # Try to move the obstacle to a new position
        new_x, new_y = x, y
        while (new_x, new_y) == (x, y) or grid[new_x][new_y] in ['S', 'T', 'X']:  # Ensure valid move
            direction = random.choice(directions)
            new_x = x + direction[0]
            new_y = y + direction[1]
            if 0 <= new_x < size and 0 <= new_y < size:  # Check bounds
                if grid[new_x][new_y] == ' ':
                    break
        
        grid[new_x][new_y] = 'X'  # Place the new obstacle
        new_obstacles.append((new_x, new_y))  # Track new position
    
    return grid, new_obstacles  # Return updated grid and obstacle positions

# Main function to play the game with moving obstacles
def treasure_hunt_moving_obstacles():
    # Ask the user for grid size and number of obstacles
    size = int(input("Enter the grid size (e.g., 6 for a 6x6 grid): "))
    num_obstacles = int(input(f"Enter the number of obstacles (less than {size * size - 2}): "))  # Make sure obstacles are less than available spaces

    # Create the grid and place the treasure randomly
    grid, goal = create_grid(size)

    # Add random obstacles to the grid and store their positions
    grid = add_obstacles(grid, num_obstacles)
    obstacles = [(i, row.index('X')) for i, row in enumerate(grid) if 'X' in row]  # Track obstacle positions

    # Print the initial grid
    print("\nInitial Grid:")
    print_grid_with_path(grid, [])  # Empty path initially

    # Start the search using A* algorithm
    print("\nSearching for the treasure using A* algorithm with moving obstacles...\n")
    path = a_star(grid, (0, 0), goal)  # Perform A* search

    # Move obstacles after each step
    for step in path:
        print(f"\nPlayer at: {step}")
        grid, obstacles = move_obstacles(grid, obstacles)  # Move obstacles
        print_grid_with_path(grid, path[:path.index(step) + 1])  # Show current progress

    # Print the final grid with the path marked
    print("\nFinal Path to the Treasure:")
    print_grid_with_path(grid, path)  # Show the path to the treasure

# Run the modified game with moving obstacles
treasure_hunt_moving_obstacles()