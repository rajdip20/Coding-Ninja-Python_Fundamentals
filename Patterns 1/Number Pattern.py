# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#   1234
#   123
#   12
#   1

N = int(input())
for i in range(N, 0, -1):
    for j in range(1, i + 1):
        print(j, end='')
    print("\r")
