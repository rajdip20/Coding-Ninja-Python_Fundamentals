# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#   4444
#   333
#   22
#   1

N = int(input())

for i in range(N+1, 0, -1):
    for j in range(0, i-1):
        print(N, end='')
    N = N-1
    print("")
