
#  Autonomous Delivery Agent

Ever wondered how a delivery drone finds its way through a busy city? This project brings that concept to life! It's a simulation of a smart delivery agent that navigates a grid-based city, dodging obstacles and tricky terrain to find the best possible path to deliver its packages.

I built this to explore the core ideas of artificial intelligence—how algorithms can make rational decisions, plan efficiently, and adapt on the fly, just like a real autonomous vehicle would.

## What Can It Do?

- ** Navigate Complex Cities:** The agent finds its way through maps filled with roads, slow-moving mud, costly water crossings, and static buildings.
- **⏱ Choose the Best Strategy:** It doesn't just find *a* path; it finds the *best* path using different AI techniques:
  - **BFS (Breadth-First Search):** Finds the shortest route by number of steps. Great for simple maps.
  - **UCS (Uniform-Cost Search):** Finds the cheapest route, avoiding expensive terrain. The reliable, cost-conscious option.
  - **A* Search:** The smart navigator! Uses a built-in "sense of direction" to find the optimal path much faster.
  - **Local Replanning:** The agile problem-solver. If a car suddenly blocks the road, it quickly finds a new detour without starting from scratch.
- **  Provide Clear Results:** For every run, it tells you the total cost of the trip, how much "thinking" it had to do, and how long it took.

##   Getting Started

### 1. Grab the Code

First, clone the project to your computer:

```bash
git clone  https://github.com/bongurishi/delivery_agent_project.git
cd delivery_agent_project
```

### 2. Run a Delivery!

Use the command line to tell the agent which map to use and how to think. It's super easy.

**Example commands:**

```bash
# Have the smart A* algorithm deliver a package on a small map
python main.py --map maps/small.grid --algorithm astar

# Test the agent's ability to react to a moving obstacle on the dynamic map
python main.py --map maps/dynamic.grid --algorithm local --dynamic
```

##  Understanding the Map Files

The city layouts are simple text files. Here’s a quick guide:

- The first line is the map size (e.g., `10 10` for a 10x10 grid).
- The following lines are the map itself, where each number is a type of terrain:
  - `0` = Road (cost 1)
  - `1` = Building (blocked!)
  - `2` = Mud (cost 3)
  - `3` = Water (cost 5)
- `S 0 0` marks the **Start** point.
- `G 9 9` marks the **Goal** point.
- `D 5 5 5` means a **Dynamic Obstacle** (like a car) will appear at position (5,5) at timestep 5.

##  Learn More & See the Results

Curious about which algorithm performed best? Want to see the graphs and my analysis?

Check out the full **`report.pdf`** included in this project! It breaks down the strengths and weaknesses of each approach and shows the data behind the performance.

---

## Contributers.
B.Rishi
Seema yadav
Jasika