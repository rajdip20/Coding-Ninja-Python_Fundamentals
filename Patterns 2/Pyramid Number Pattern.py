# Print the following pattern for the given number of rows.
# Pattern for N = 4
#      1
#     212
#    32123
#   4321234

row = int(input())

for i in range(1, row+1):

    for j in range(1, row+1-i):
        print(' ', end='')

    for j in range(i, 0, -1):
        print(j, end='')

    for j in range(2, i+1):
        print(j, end='')

    print()
