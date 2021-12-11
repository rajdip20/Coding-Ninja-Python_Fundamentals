# Print the following pattern for the given number of rows.
# Note: N is always odd.

# Pattern for N = 5
#     *
#    ***
#   *****
#    ***
#     *

def display(n):
    sp = n // 2
    st = 1
    for i in range(1, n + 1):
        for j in range(1, sp + 1):
            print(" ", end='')
        count = st // 2 + 1
        for k in range(1, st + 1):
            print("*", end='')
            if (k <= (st // 2)):
                count -= 1
            else:
                count += 1

        print()
        
        if (i <= n // 2):
            sp -= 1
            st += 2
        else:
            sp += 1
            st -= 2


n = int(input())
display(n)
