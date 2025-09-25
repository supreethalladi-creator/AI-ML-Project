import heapq, time
from collections import deque

def bfs(grid,start,goal):
    t0=time.time()
    frontier=deque([start]); came={start:None}
    nodes=0
    while frontier:
        cur=frontier.popleft(); nodes+=1
        if cur==goal: break
        r,c=cur
        for nr,nc in grid.neighbors(r,c):
            if (nr,nc) not in came and grid.is_passable(nr,nc):
                came[(nr,nc)]=cur; frontier.append((nr,nc))
    path=_reconstruct(came,start,goal)
    cost=sum(grid.cost(r,c) for r,c in path) if path else float('inf')
    return {'path':path,'cost':cost,'nodes_expanded':nodes,'time':time.time()-t0}
def astar(grid,start,goal):
    def manhattan(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
    t0=time.time(); frontier=[(0,start)]
    came={start:None}; cost={start:0}; nodes=0
    while frontier:
        _,cur=heapq.heappop(frontier); nodes+=1
        if cur==goal: break
        r,c=cur
        for nr,nc in grid.neighbors(r,c):
            if not grid.is_passable(nr,nc): continue
            newc=cost[cur]+grid.cost(nr,nc)
            if (nr,nc) not in cost or newc<cost[(nr,nc)]:
                cost[(nr,nc)]=newc; came[(nr,nc)]=cur
                heapq.heappush(frontier,(newc+manhattan((nr,nc),goal),(nr,nc)))
    path=_reconstruct(came,start,goal)
    return {'path':path,'cost':cost.get(goal,float('inf')),'nodes_expanded':nodes,'time':time.time()-t0}
def ucs(grid,start,goal): return astar(grid,start,goal)
def local_search_replan(grid,start,goal,**kw): return astar(grid,start,goal)
def _reconstruct(came,start,goal):
    if goal not in came: return []
    cur=goal; path=[]
    while cur is not None: path.append(cur); cur=came[cur]
    return path[::-1]
