# For a given string(str), remove all the consecutive duplicate characters.

s = input()
s = s+" "
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        print(s[i], end="")
