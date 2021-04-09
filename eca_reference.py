# Reference: https://matplotlib.org/matplotblog/posts/elementary-cellular-automata/

import numpy as np

rng = np.random.RandomState(42)
data = rng.randint(0,2,20)

# prints random num from seed state 42 in array size (20) with numbbers 0 & 1
print(data)

# a given cell C only knows about the state of it's left and right neighbors
# labeled L and R respectively. We can define a function or rule, f(L, C, R)
# which maps the cell state to either 0 or 1

# Input cells are binary values there are 2^3 = 8 possible inputs into fxn

# prints binary representation of size 3 8 times (2^3 = 8)
for i in range(8):
    print(np.binary_repr(i,3))
    
# assign 0 or 1 to each input triplet. Output of f is the value which will 
# replace the current cell C in the next time step. In total there are 2^2^3 = 2^8 = 256
# possible rules for updating a cell. Known as wolfram code, for the update rules in which 
# rule is represented by an 8 bit binary number.

# Example "Rule 30" could be constructed by first converting to binary and then building
# an array for each bit

# assign number to 30
rule_number = 30
# rule string = binary representation of 30 in size 8
rule_string = np.binary_repr(rule_number, 8)
# turn rule_string into an array of size 8 
rule = np.array([int(bit) for bit in rule_string])

print(rule, rule_string, rule_number)

# Wolfram code associates the leading bit with '111' and the final bit with '000'
# for rule 30 the relationship between the input, rule index and output is as follows

for i in range(8):
    triplet = np.binary_repr(i,3)
    print(f"input: {triplet}, index: {7-i}, output {rule[7-i]}")
    
# can define a fxn which maps the input cell info with the associated rule index
# essentially we convert the binary input to decimal and adjust the index range

# returns the output value at the specified index
def rule_index(triplet):
    L, C, R = triplet
    index = 7 - (4*L + 2*C + R)
    return int(index)

# returns output 0 from index 2 ('101')
print(rule[rule_index((1,0,1))])

# finally use numpy to create a data struct containing all the triplets
# for our state array and apply the fxn across the appropriate axis to 
# determine our new state.

# honestly don't get this but come back and try to when everything is done
all_triplets = np.stack([
    np.roll(data, 1), 
    data,
    np.roll(data, -1)
])

# prints single update of our cellular automata
new_data = rule[np.apply_along_axis(rule_index,0,all_triplets)]
print(new_data)

# To do many updates and record the state over time, we will create a fxn
# aka all together now
def CA_run(initial_state, n_steps, rule_number):
    rule_string = np.binary_repr(rule_number, 8)
    rule = np.array([int(bit) for bit in rule_string])
    
    m_cells = len(initial_state)
    CA_run = np.zeros((n_steps, m_cells))
    CA_run[0, :] = initial_state
    
    for step in range(1, n_steps):
        all_triplets = np.stack(
            [
                np.roll(CA_run[step - 1, :], 1),
                CA_run[step - 1, :],
                np.roll(CA_run[step - 1, :], -1),
            ]
        )
        CA_run[step, :] = rule[np.apply_along_axis(rule_index, 0, all_triplets)]
    
    return CA_run

initial = np.array([0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0])
data = CA_run(initial, 10, 30)
print(data)

# now visiuals since line 102 only gives us binary representation of the results

import matplotlib.pyplot as plt 
# color map using binary
plt.rcParams['image.cmap'] = 'binary'

rng = np.random.RandomState(0)
data = CA_run(rng.randint(0, 2, 100), 50, 173)

# This makes a pyramid, test it out as needed
#initial = np.zeros(300)
#initial[300//2] = 1
#data = CA_run(initial, 150, 30)

# set figure size
fig, ax = plt.subplots(figsize=(10, 5))
# plot values of a 2d matrix/array as color-coded image.
ax.matshow(data)
# take off axis numbers
ax.axis(False);
# show the plotted graph
plt.show()
