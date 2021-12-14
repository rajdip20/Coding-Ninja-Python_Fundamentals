# Print the following pattern for the given number of rows.
# Pattern for N = 5
#   1 2 3 4 5
#   11 12 13 14 15
#   21 22 23 24 25
#   16 17 18 19 20
#   6 7 8 9 10


def pattern(n):
    mid = (n >> 1)
    if n & 1 != 0:
        mid += 1
    val = 1
    for i in range(mid):
        for j in range(val, val + n):
            print(j, end=' ')
        print()
        val += (n << 1)
    if n & 1 != 0:
        val -= (n << 1)
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)
    else:
        val -= n
        for i in range(mid, n):
            for j in range(val, val + n):
                print(j, end=' ')
            print()
            val -= (n << 1)


n = int(input())
pattern(n)
