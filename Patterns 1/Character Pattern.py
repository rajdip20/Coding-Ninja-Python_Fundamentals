# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#   A
#   BC
#   CDE
#   DEFG

N = int(input())
i = 1
stop = 2
for i in range(N):
    column = 1
    start = chr(ord('A')+i-1)
    for column in range(1, stop):
        charp = chr(ord(start)+column)
        print(charp, end='')
    print("")
    stop += 1
