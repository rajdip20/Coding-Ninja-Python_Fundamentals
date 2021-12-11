# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#   1
#   11
#   202
#   3003

N = int(input())
for i in range(1, N+1):
    for j in range(0, i):
        x = i-1
        if x == 0:
            print(1, end="")
        else:
            if x == j or j == 0:
                print(x, end="")
            else:
                print(0, end="")
    print("")
