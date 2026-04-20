import random


class GameOfLife:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.grid = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(0)
            self.grid.append(row)

    def randomize(self, p=0.3):
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < p:
                    self.grid[y][x] = 1
                else:
                    self.grid[y][x] = 0

    def count_neighbors(self, x, y):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx = x + dx
                ny = y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    count += self.grid[ny][nx]
        return count

    def step( self ):
     new_grid=[];h=self.height;w=self.width;g=self.grid
     for y in range(h):
      row=[]
      for x in range(w):
       n=0
       for dy in [-1,0,1]:
        for dx in [-1,0,1]:
         if dx==0 and dy==0: continue
         nx=x+dx;ny=y+dy
         if 0<=nx<w and 0<=ny<h:
          n+=g[ny][nx]
       cell=g[y][x]
       if cell==1:
        if n<2:row.append(0)
        elif n==2 or n==3:row.append(1)
        else: row.append(0)
       else:
        if n==3: row.append(1)
        else: row.append(0)
      new_grid.append(row)
     self.grid=new_grid

    def set_pattern(self, cells):
        for x, y in cells:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = 1

    def clear(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = 0

    def as_text(self):
        lines = []
        for row in self.grid:
            s = ""
            for cell in row:
                if cell == 1:
                    s += "#"
                else:
                    s += "."
            lines.append(s)
        return "\n".join(lines)
