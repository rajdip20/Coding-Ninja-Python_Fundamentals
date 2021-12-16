# Print the following pattern
# Pattern for N = 4
#      *
#     ***
#    *****
#   *******

N = int(input())
k = 0

for i in range(1, N+1):
    for space in range(1, (N-i)+1):
        print(end=" ")
    while k != (2*i-1):
        print("*", end="")
        k = k + 1
    k = 0
    print()
