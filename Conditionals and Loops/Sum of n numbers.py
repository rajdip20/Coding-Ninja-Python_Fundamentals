# Given an integer n, find and print the sum of numbers from 1 to n.

n = int(input())
x = 0

if(1 <= n <= 100):
    for i in range(1, n+1):
        x = i+x
    print(x)
