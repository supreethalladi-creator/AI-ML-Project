# Project Report (max 6 pages)

## Title
Autonomous Delivery Agent on 2D Grid

## Abstract (≤ 200 words)
A short summary of the environment, goals, and results.

## 1. Environment Model
- Grid details, cell costs, static and dynamic obstacles.
- Map file format (rows cols followed by grid).

## 2. Agent Design
- Movement model (4-connected), cost model, replanning horizon.

## 3. Algorithms Implemented
- BFS / Uniform Cost Search
- A* with admissible heuristic (Manhattan)
- Local search replanning (Simulated Annealing / Hill-Climbing)

## 4. Experimental Setup
- Describe map sizes (small/medium/large/dynamic), metrics (path cost, nodes expanded, time).

## 5. Results
- Tables: three planners × four maps (path cost, nodes expanded, time)
- Include short plots (generated with matplotlib).

## 6. Analysis and Conclusion
- When each algorithm performs better and why.
- Limitations and future work.
