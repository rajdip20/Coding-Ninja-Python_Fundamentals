# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.

# Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

N = int(input())
rev = 0

while(N > 0):
    a = N % 10
    rev = rev * 10 + a
    N = N // 10

print(rev)
