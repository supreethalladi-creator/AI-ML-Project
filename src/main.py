import argparse
import os
import matplotlib.pyplot as plt
from grid import Grid
from planners import bfs, ucs, astar, local_search_replan

try:
    from viz import visualize
except ImportError:
    visualize = None


def parse_args():
    p = argparse.ArgumentParser(description='Autonomous Delivery Agent - Run planners')
    p.add_argument('--planner', choices=['bfs', 'ucs', 'astar', 'local'], default='astar')
    p.add_argument('--map', required=True)
    p.add_argument('--start', nargs=2, type=int, required=True, help='start r c (0-indexed)')
    p.add_argument('--goal', nargs=2, type=int, required=True, help='goal r c (0-indexed)')
    p.add_argument('--show', action='store_true', help='Show ASCII map with path')
    p.add_argument('--viz', action='store_true', help='Visualize path with matplotlib')
    p.add_argument('--record_log', type=str, default=None, help='Save run log to file')
    p.add_argument('--record_video', type=str, default=None, help='Save animation as MP4 or GIF (stored in demos/)')
    p.add_argument('--horizon', type=int, default=5, help='planning horizon for dynamic scenarios')
    return p.parse_args()


def ascii_show(grid, path):
    chars = [['.' if grid.grid[r][c] > 0 else '#' for c in range(grid.cols)] for r in range(grid.rows)]
    for r in range(grid.rows):
        for c in range(grid.cols):
            if grid.grid[r][c] > 1:
                chars[r][c] = str(grid.grid[r][c])
    if path:
        for (r, c) in path:
            chars[r][c] = '*'
    print('\n'.join(''.join(row) for row in chars))


def save_graphs(results, algo_name):
    """Save bar charts of cost, nodes expanded, and execution time into demos/ folder"""
    demo_dir = os.path.join(os.getcwd(), "demos")
    os.makedirs(demo_dir, exist_ok=True)

    # Path cost
    plt.figure(figsize=(4, 3))
    plt.bar([algo_name], [results['cost']], color='orange')
    plt.title("Path Cost")
    plt.ylabel("Cost")
    plt.savefig(os.path.join(demo_dir, f"{algo_name}_path_cost.png"))
    plt.close()

    # Nodes expanded
    plt.figure(figsize=(4, 3))
    plt.bar([algo_name], [results['nodes_expanded']], color='blue')
    plt.title("Nodes Expanded")
    plt.ylabel("Nodes")
    plt.savefig(os.path.join(demo_dir, f"{algo_name}_nodes_expanded.png"))
    plt.close()

    # Execution time
    plt.figure(figsize=(4, 3))
    plt.bar([algo_name], [results['time']], color='green')
    plt.title("Execution Time")
    plt.ylabel("Seconds")
    plt.savefig(os.path.join(demo_dir, f"{algo_name}_execution_time.png"))
    plt.close()

    print(f"Saved graphs for {algo_name} in {demo_dir}")


def run():
    args = parse_args()
    grid = Grid.load_from_file(args.map)
    start = tuple(args.start)
    goal = tuple(args.goal)
    planner_name = args.planner
    planner = {'bfs': bfs, 'ucs': ucs, 'astar': astar, 'local': local_search_replan}[planner_name]

    print(f"Running planner={planner_name} on map={args.map} start={start} goal={goal}")
    res = planner(grid, start, goal) if planner_name != 'local' else planner(grid, start, goal, max_iters=500, temp=1.0)

    print('Result summary:')
    print(f"  Path length (nodes): {len(res['path'])}")
    print(f"  Path cost: {res['cost']}")
    print(f"  Nodes expanded: {res['nodes_expanded']}")
    print(f"  Time (s): {res['time']:.4f}")

    if args.record_log:
        with open(args.record_log, 'w') as f:
            f.write(str(res))
        print(f"Wrote log to {args.record_log}")

    if args.show:
        ascii_show(grid, res['path'])

    if args.viz and visualize:
        # auto-organize videos inside demos/
        if args.record_video:
            demo_dir = os.path.join(os.getcwd(), "demos")
            os.makedirs(demo_dir, exist_ok=True)
            save_path = os.path.join(demo_dir, os.path.basename(args.record_video))
        else:
            save_path = None
    
        visualize(grid, res['path'], start, goal, grid.dynamic_schedule, animate=True, record_file=save_path)
        plt.text(0.5, 0.5, "BMYLR", fontsize=30, color='gray',
         ha='center', va='center', alpha=0.2, rotation=30,
         transform=plt.gca().transAxes)

    # Save graphs automatically
    save_graphs(res, planner_name)

    return res


if __name__ == '__main__':
    run()
