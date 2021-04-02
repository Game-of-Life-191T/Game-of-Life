# ------------------------- #
# Game of Life 191T Project #
# ------------------------- #
#     Mitchell Maltezo      #
#      Michael Spohn        #
#     Rosellyn Vicente      #
#       Pranav Arora        #
# ------------------------- #

# Custom rule set
rule = -1
while rule < 1 or rule > 256:
    print("Enter rule number (1-256):")
    rule = input()
    rule = int(rule)
    if rule > 0 and rule < 257:
        rule = rule - 1
        break
    print("Error, please retype your input")

# Rule in binary list
setrule = [0, 0, 0, 0, 0, 0, 0, 0]
q = rule
r = 0
for i in setrule:
    q = q / 2
    r = q % 2
    if r == 0:
        setrule[i] = 0
    else:
        setrule[i] = 1
        if q == 1:
            break
    
for i in setrule:
    print(setrule[7-i])


