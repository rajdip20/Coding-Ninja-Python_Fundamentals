# You are given two integers: X and N. You have to calculate X raised to power N and print it.

X = int(input())
N = int(input())

if(1<=X<=100 and 1<=N<=10):
    a = X**N
    print(a)
