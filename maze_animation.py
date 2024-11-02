import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the Maze Environment (0 = free, 1 = wall, 2 = goal)
maze = np.array([
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 2]
])

# Define start and goal positions
start_pos = (0, 0)  # Top-left corner
goal_pos = (6, 6)   # Bottom-right corner marked by '2'

# Agent position
agent_pos = list(start_pos)

# Movements (down, up, right, left)
moves = {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

# Function to check if the move is valid
def is_valid_move(pos):
    r, c = pos
    return 0 <= r < maze.shape[0] and 0 <= c < maze.shape[1] and maze[r, c] != 1

# Create a figure for the animation
fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])

# Function to update the agent's position in the maze
def update(num):
    global agent_pos
    ax.clear()
    ax.imshow(maze, cmap="Blues")

    if agent_pos == goal_pos:
        ax.text(0.5, -0.1, "Goal Reached!", ha="center", transform=ax.transAxes, fontsize=12, color="green")
        return

    # Randomly choose a valid move
    move_name = np.random.choice(list(moves.keys()))
    new_pos = (agent_pos[0] + moves[move_name][0], agent_pos[1] + moves[move_name][1])
    if is_valid_move(new_pos):
        agent_pos = new_pos

    # Show the agent's current position
    maze_copy = maze.copy()
    maze_copy[agent_pos] = 3  # Mark the agent position
    ax.imshow(maze_copy, cmap="Blues")

# Run the animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=200)

# Save as a video file
output_path = "maze_solving_animation.gif"
ani.save(output_path, writer="imagemagick", dpi=150)

