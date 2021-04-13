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
DYING = 1
vals = [ON, DYING, OFF]

# populate grid with random values
#grid = np.random.choice(vals, N*N, p=[0.1,0.1,0.8]).reshape(N, N)

# for all OFF values to test other objects, comment out line 24 and uncomment line 26
grid = np.random.choice(vals, N*N, p=[0,0,1]).reshape(N, N)


# Delete quotations for glider
test = [[OFF, ON, DYING, OFF, OFF],
        [DYING, OFF, OFF, ON, OFF],
        [ON, OFF, OFF, DYING, OFF],
        [OFF, DYING, ON, OFF, OFF]]

grid[1:5, 1:6] = test

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
      # black = alive
      # grey = dying
      # white = dead   
      if grid[i, j] == ON:       # if alive, start dying
          newGrid[i, j] = DYING     
      elif grid[i, j] == DYING:     # if dying, die
          newGrid[i, j] = OFF
      else:    # else if dead, and alive neighbors total 2, then become alive
          if grid[i, j] == OFF:
              if total >= 2 and total < 3:
                newGrid[i, j] = ON  
          
  # update data
  tempGrid = newGrid.copy()
  for i in range(N):
        for j in range(N):
              if tempGrid[i, j] == 1:
                    tempGrid[i, j] = 128
  mat.set_data(tempGrid)
  grid = newGrid
  return [mat]

# set animation
fig, ax = plt.subplots()
plt.rcParams['image.cmap'] = 'binary'
tempGrid = grid.copy()
for i in range(N):
      for j in range(N):
             if tempGrid[i, j] == 1:
                   tempGrid[i, j] = 128
mat = ax.matshow(tempGrid)
ani = animation.FuncAnimation(fig, update, interval=1000,
                              save_count=1000)
plt.show()