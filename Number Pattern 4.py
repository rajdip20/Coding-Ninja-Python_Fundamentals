# Print the following pattern for n number of rows.
#For eg. N = 5

#   1        1
#   12      21
#   123    321
#   1234  4321
#   1234554321

num = int(input())
i = 1
while num >= i:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1

    space = 1
    spaces = 1
    while spaces <= (num-i):
        print(" ", end="")
        spaces = spaces+1
    spaces = 1
    while spaces <= (num-i):
        print(" ", end="")
        spaces = spaces+1
    k = i
    while k >= 1:
        print(k, end="")
        k = k-1
    print()
    i += 1
