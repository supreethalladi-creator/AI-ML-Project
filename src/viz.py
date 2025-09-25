"""
viz.py
Visualization and animation of the grid, path, and dynamic obstacles using matplotlib.
Supports saving demo as .mp4 or .gif.
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def visualize(grid, path, start, goal, dynamic_schedule=None, animate=False, interval=500, record_file=None):
    rows, cols = grid.rows, grid.cols
    base = np.ones((rows, cols, 3))

    # map terrain costs to colors
    for r in range(rows):
        for c in range(cols):
            if grid.grid[r][c] == 0:
                base[r, c] = [0, 0, 0]   # black for obstacle
            elif grid.grid[r][c] == 1:
                base[r, c] = [1, 1, 1]   # white for cost 1
            else:
                base[r, c] = [1, 1-(grid.grid[r][c]*0.1), 1-(grid.grid[r][c]*0.1)]

    fig, ax = plt.subplots()

    # overlay start and goal
    ax.scatter(start[1], start[0], c='blue', marker='o', s=100, label='Start')
    ax.scatter(goal[1], goal[0], c='red', marker='X', s=100, label='Goal')
    ax.legend(loc='upper right')

    if not animate:
        if path:
            y = [p[0] for p in path]
            x = [p[1] for p in path]
            ax.imshow(base, interpolation='nearest')
            ax.plot(x, y, c='green')
        if record_file:
            plt.savefig(record_file)
            print(f"Saved static visualization to {record_file}")
        else:
            plt.show()
        return

    # animate movement along path
    path = path or []

    def update(frame):
        ax.clear()
        ax.imshow(base, interpolation='nearest')
        ax.scatter(start[1], start[0], c='blue', marker='o', s=100)
        ax.scatter(goal[1], goal[0], c='red', marker='X', s=100)
        # draw obstacles if dynamic schedule
        if dynamic_schedule and frame in dynamic_schedule:
            for (r, c) in dynamic_schedule[frame]:
                ax.scatter(c, r, c='black', marker='s', s=80)
        if frame < len(path):
            subpath = path[:frame+1]
            y = [p[0] for p in subpath]
            x = [p[1] for p in subpath]
            ax.plot(x, y, c='green')
            ax.plot(path[frame][1], path[frame][0], 'go', markersize=12)
        ax.set_title(f"Step {frame}")

    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=interval, repeat=False)

    if record_file:
        ani.save(record_file)
        print(f"Saved animation to {record_file}")
    else:
        plt.show()

