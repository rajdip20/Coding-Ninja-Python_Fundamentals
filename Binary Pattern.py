# Print the following pattern for the given number of rows.
# Pattern for N = 4
#   1111
#   000
#   11
#   0

N = int(input())

for i in range(0, N):
    for j in range(0, N - i):
        if(i % 2 == 0):
            print(1, end='')
        else:
            print(0, end='')
    print()
