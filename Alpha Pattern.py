# Print the following pattern for the given N number of rows.
# Pattern for N = 3
#   A
#   BB
#   CCC

ascii_number = 65
N = int(input())
for i in range(0, N):
    for j in range(0, i+1):
        character = chr(ascii_number)
        print(character, end='')
    ascii_number += 1
    print("")
