from typing import List, Tuple
class Grid:
    def __init__(self, grid, dynamic_schedule=None):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows>0 else 0
        self.dynamic_schedule = dynamic_schedule or {}
    def in_bounds(self, r,c): return 0<=r<self.rows and 0<=c<self.cols
    def is_passable(self,r,c,time=None):
        if not self.in_bounds(r,c) or self.grid[r][c]==0: return False
        if time is not None and time in self.dynamic_schedule and (r,c) in self.dynamic_schedule[time]: return False
        return True
    def cost(self,r,c): return self.grid[r][c]
    @classmethod
    def load_from_file(cls,path):
        static=[];dynamic={}
        with open(path) as f: lines=[ln.strip() for ln in f if ln.strip()]
        rows,cols=map(int,lines[0].split())
        for i in range(1,1+rows): static.append([int(x) for x in lines[i].split()])
        for ln in lines[1+rows:]:
            if ln.startswith('D:'):
                t,r,c=map(int,ln[2:].split())
                dynamic.setdefault(t,set()).add((r,c))
        return cls(static,dynamic)
    def neighbors(self,r,c):
        for dr,dc in ((-1,0),(1,0),(0,-1),(0,1)):
            nr,nc=r+dr,c+dc
            if self.in_bounds(nr,nc) and self.grid[nr][nc]!=0: yield (nr,nc)
