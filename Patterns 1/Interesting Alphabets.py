# Print the following pattern for the given number of rows.
# Pattern for N = 5
#   E
#   DE
#   CDE
#   BCDE
#   ABCDE

N = int(input())
a = 64
it = 0
for i in range(N, 0, -1):
    while(N >= i):
        print(chr(a+i), end="")
        i = i+1
    print()
