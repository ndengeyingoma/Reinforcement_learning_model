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

# Initialize the text box for learning messages
learning_text = ax.text(0.5, -0.1, '', ha="center", transform=ax.transAxes, fontsize=12, color="blue")

# Function to update the agent's position in the maze
def update(num):
    global agent_pos
    ax.clear()
    ax.imshow(maze, cmap="Blues")

    if agent_pos == goal_pos:
        ax.text(0.5, -0.1, "Goal Reached!", ha="center", transform=ax.transAxes, fontsize=12, color="green")
        return

    # Randomly choose a valid move and check if it's hitting a wall or moving closer to the goal
    move_name = np.random.choice(list(moves.keys()))
    new_pos = (agent_pos[0] + moves[move_name][0], agent_pos[1] + moves[move_name][1])

    if is_valid_move(new_pos):
        # If the move is valid, update the agent's position
        agent_pos = new_pos
        learning_text.set_text("Exploring")  # Indicate that the agent is exploring
    else:
        # If the move is invalid, keep the position and set the message to learning from error
        learning_text.set_text("Learning from Error")

    # Show the agent's current position
    maze_copy = maze.copy()
    maze_copy[agent_pos] = 3  # Mark the agent position
    ax.imshow(maze_copy, cmap="Blues")
    ax.text(0.5, -0.1, learning_text.get_text(), ha="center", transform=ax.transAxes, fontsize=12, color="blue")

# Run the animation
ani = animation.FuncAnimation(fig, update, frames=50, interval=200)

# Save as a video file or GIF
output_path = "maze_solving_animation.gif"
ani.save(output_path, writer="pillow", dpi=150)
