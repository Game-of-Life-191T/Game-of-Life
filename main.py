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

setrule = []