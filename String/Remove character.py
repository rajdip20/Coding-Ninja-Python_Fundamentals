# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.

# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

s = input()
r = input()
for i in range(len(s)):
    if s[i] != r:
        print(s[i], end="")
