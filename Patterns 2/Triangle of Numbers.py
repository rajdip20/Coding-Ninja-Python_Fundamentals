# Print the following pattern for the given number of rows.
# Pattern for N = 4
#      1
#     232
#    34543
#   4567654

N = int(input())
num = 1
gap = N - 1
for j in range(1, N + 1):
    num = j
    for i in range(1, gap + 1):
        print(" ", end="")
    gap = gap - 1

    for i in range(1, j + 1):
        print(num, end="")
        num = num + 1

    num = num - 2
    for i in range(1, j):
        print(num, end="")
        num = num - 1

    print()
