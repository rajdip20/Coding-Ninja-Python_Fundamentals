# Print the following pattern for the given N number of rows.
# Pattern for N = 4
#      1
#     12
#    123
#   1234

N = int(input())
i = 1

while i <= N:
    s = 1
    while s <= N-i:
        print(" ", end='')
        s = s+1
    num = 1
    while num <= i:
        print(num, end='')
        num = num+1
    print('')
    i = i + 1
