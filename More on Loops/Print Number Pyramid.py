# Print the following pattern for a given n.
# For eg. N = 6
#   123456
#    23456
#     3456
#      456
#       56
#        6
#       56
#      456
#     3456
#    23456
#   123456

num = int(input())
i = 0
while num > i:
    spaces = 1
    while spaces <= i:
        print(" ", end="")
        spaces = spaces+1
    j = 1
    while num-i >= j:
        print(j+i, end="")
        j = j+1
    i = i+1
    print()
while i > 1:
    spaces = 1
    while spaces <= i-2:
        print(" ", end="")
        spaces = spaces+1
    j = num
    k = 1
    while j >= i-1:
        print(i+k-2, end="")
        j = j-1
        k = k+1

    i = i-1
    print()
