# Main file for Elementary Cellular Automata implementations
# 
# Handled by Michael Spohn and Mitchell Maltezo
# 
# Game of Life Project - Return to M O N K E
#
# Reference: https://matplotlib.org/matplotblog/posts/elementary-cellular-automata/

import numpy as np
import matplotlib.pyplot as plt

# returns the output value at the specified index
def rule_index(triplet):
    L, C, R = triplet
    index = 7 - (4*L + 2*C + R)
    return int(index)

# Fxn that takes in an intial state, steps that is initial.size/2, and a wolfram rule number 
# and returns a 2D array of the results of each step/iteration by recursion
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


# color map using binary
plt.rcParams['image.cmap'] = 'binary'
"""
rng = np.random.RandomState(0)
data = CA_run(rng.randint(0, 2, 100), 50, 110)

# Pyramid pattern
initial = np.zeros(300)
initial[300//2] = 1
data = CA_run(initial, 150, 30)

# set figure size
fig, ax = plt.subplots(figsize=(10, 5))
# plot values of a 2d matrix/array as color-coded image.
ax.matshow(data)
# take off axis numbers
ax.axis(False);
# show the plotted graph
plt.show()
"""

def plot_CA_class(rule_list, class_label):
    rng = np.random.RandomState(seed=0)
    fig, axs = plt.subplots(1, len(rule_list),figsize=(10, 3.5), constrained_layout=True)
    initial = rng.randint(0, 2, 100)

    for i, ax in enumerate(axs.ravel()):
        data = CA_run(initial, 100, rule_list[i])
        ax.set_title(f'Rule {rule_list[i]}')
        ax.matshow(data)
        ax.axis(False)

    fig.suptitle(class_label, fontsize=16)

    return fig, ax
    
_ = plot_CA_class([110, 4, 30, 72, 90], 'Results 1')
plt.show()

_ = plot_CA_class([26, 57, 129, 193, 105], 'Results 2')
plt.show()
