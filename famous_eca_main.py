# Main file for Brian's Brain | CSCI 191T
# 
# Handled by Michael Spohn and Mitchell Maltezo
# 
# Game of Life Project - Return to M O N K E
#
# Reference: https://electronut.in/simple-python-matplotlib-implementation-of-conways-game-of-life/
#              -- Similar to the link but change the rules to fit Brian's brain rules rather than conway's GoL
#              Rules:
#              -- 1. If alive, set to dying
#              -- 2. If dying, set to dead
#              -- 3. If dead, and alive neighbors == 2, set to alive


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 10
ON = 256
OFF = 0
DYING = 128
vals = [ON, DYING, OFF]

# populate grid with random values
grid = np.random.choice(vals, N*N, p=[0.4,0.1,0.5]).reshape(N, N)

# for all OFF values to test other objects, comment out line 24 and uncomment line 26
#grid = np.random.choice(vals, N*N, p=[0,0,1]).reshape(N, N)


# Delete quotations for oscillator
"""osc = [[OFF, ON, DYING, OFF, OFF],
        [DYING, OFF, OFF, ON, OFF],
        [ON, OFF, OFF, DYING, OFF],
        [OFF, DYING, ON, OFF, OFF]]

grid[1:5, 1:6] = osc
"""
def update(data):
  global grid
  # copy grid since we require 8 neighbors for calculation
  # iterate line by line
  newGrid = grid.copy()
  for i in range(N):
    for j in range(N):
      # compute 8-neighbor sum (Add the amount of live/dying/dead cells around the current cell)
      # using toroidal boundary conditions - x and y wrap around current position
      total = (grid[i, (j-1)%N] + grid[i, (j+1)%N] + 
               grid[(i-1)%N, j] + grid[(i+1)%N, j] + 
               grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + 
               grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N])/256
      
      # apply Brian's brain rules based on total (kind of)      
      # 1 = alive
      # 3 = dying
      # 0 = dead   
      if grid[i, j] == ON:       # if alive, start dying
          newGrid[i, j] = DYING     
      elif grid[i, j] == DYING:     # if dying, die
          newGrid[i, j] = OFF    
      elif grid[i, j] == OFF:   # else if dead, and alive neighbors total 2, then become alive
          if total >= 2 and total < 4:
            newGrid[i, j] = ON  
          
  # update data
  mat.set_data(newGrid)
  grid = newGrid
  return [mat]

# set animation
plt.rcParams['image.cmap'] = 'binary'
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=10000,
                              save_count=10000)
plt.show()