# Example commands

# 1) Run A* on small map and print path:
python src/main.py --planner astar --map maps/small.map --start 1 1 --goal 4 4 --viz

# 2) Run Uniform Cost Search:
python src/main.py --planner ucs --map maps/medium.map --start 1 1 --goal 12 12 --viz

# 3) Run BFS (treat cost as uniform):
python src/main.py --planner bfs --map maps/small.map --start 1 1 --goal 8 8 --viz

# 4) Demonstrate dynamic replanning (simulated annealing local search):
python src/main.py --planner local --map maps/dynamic.map --start 1 1 --goal 14 14 --viz
